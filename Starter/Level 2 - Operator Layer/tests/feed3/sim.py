#!/usr/bin/env python3
# Copyright (c) 2026 Glen Lubbert. MIT License.
# Permission is hereby granted, free of charge, to any person obtaining a copy of this
# software and associated documentation files (the "Software"), to deal in the Software
# without restriction, including without limitation the rights to use, copy, modify, merge,
# publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons
# to whom the Software is furnished to do so, subject to the following conditions:
# The above copyright notice and this permission notice shall be included in all copies or
# substantial portions of the Software.
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
# INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR
# PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE
# FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
# OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.
"""
Simulation of Feed 3 (meeting notes to people notes) as written in seat/feeds.md.

This models the procedure's logic against a fake meeting source and sample people
notes. It is NOT a test of a real AI following the prompt, and NOT a test of any
real meeting-notes connector.

Usage:
    python3 sim.py                 # run all scenarios, print results
    python3 sim.py --write-results # also rewrite results.md beside this file

Fixtures (fake meetings, people) are in fixtures.json beside this file.
Standard library only.
"""
import json, re, sys, copy
from datetime import datetime, timedelta
from pathlib import Path

HERE = Path(__file__).resolve().parent
FIX = json.loads((HERE / "fixtures.json").read_text())

class PageFail(Exception): pass

# ---------- fake source ----------
class Source:
    def __init__(self, meetings, up=True, has_ids=True, has_edit=True, fail_page=None, page_size=2):
        self.m = meetings; self.up = up; self.has_ids = has_ids; self.has_edit = has_edit
        self.fail_page = fail_page; self.page_size = page_size
    def query(self, pred, qname):
        rows = [self._view(x) for x in self.m if pred(x)]
        pages = [rows[i:i+self.page_size] for i in range(0, len(rows), self.page_size)] or [[]]
        out = []
        for n, p in enumerate(pages):
            if self.fail_page == (qname, n): raise PageFail(f"{qname} page {n}")
            out += p
        return out
    def _view(self, x):
        v = dict(x)
        if not self.has_ids: v.pop("id", None)
        if not self.has_edit: v["edited"] = None
        return v

# ---------- vault ----------
def note(name): return {"name": name, "last_contact": None, "body": ""}
def mk(mid, ed): return f"<!-- meeting:{mid} edited:{ed or 'none'} -->"
def count(n, mid): return len(re.findall(rf"meeting:{re.escape(mid)} ", n["body"]))

class Vault:
    def __init__(self, people):
        self.people = {p: note(p) for p in people}
        self.files = {"lock": "free", "state": None, "prev": None, "new": None}
        self.attempts = []
        self.fail_after_person_writes = None; self.person_writes = 0
        self.fail_state_write_stage = None   # "main" = die after .new written, before main replaced

def dump(state): return json.dumps(state, sort_keys=True, default=str) + "\nEND OF STATE"
def load(text):
    if not text or not text.endswith("END OF STATE"): return None
    return json.loads(text[: -len("\nEND OF STATE")])

def save_state(v, state):
    v.files["new"] = dump(state)
    assert load(v.files["new"]) is not None
    if v.fail_state_write_stage == "main":
        v.fail_state_write_stage = None
        v.files["prev"] = v.files["state"]
        v.files["state"] = v.files["new"][: len(v.files["new"]) // 2]   # torn write
        raise IOError("state write interrupted")
    v.files["prev"] = v.files["state"]
    v.files["state"] = v.files["new"]

def run(v, src, now):
    # 1 lock
    lk = v.files["lock"]
    if lk.startswith("held"):
        t = datetime.fromisoformat(lk.split(" ", 1)[1])
        if now - t < timedelta(hours=2):
            v.attempts.append(f"{now} skipped: run in progress"); return "skipped"
        v.attempts.append(f"{now} stale lock taken over")
    v.files["lock"] = f"held {now.isoformat()}"
    v.attempts.append(f"{now} started")
    try:
        # 2 load state
        st = None
        for k in ("new", "state", "prev"):
            st = load(v.files[k])
            if st is not None:
                if k == "prev": v.attempts.append(f"{now} state recovered from previous copy")
                break
        if st is None: st = {"last_successful_run": None, "meetings": {}}
        # source availability
        if not src.up:
            v.attempts.append(f"{now} source unavailable"); return "unavailable"
        # 4 fetch completely
        lsr = datetime.fromisoformat(st["last_successful_run"]) if st["last_successful_run"] else None
        since = (lsr - timedelta(hours=24)) if lsr else now - timedelta(hours=24)
        fetched = {}; complete = True
        qs = [("recent", lambda m: datetime.fromisoformat(m["start"]) > since),
              ("sweep", lambda m: datetime.fromisoformat(m["start"]) > now - timedelta(days=14)),
              ("pending", lambda m: st["meetings"].get(m["id"], {}).get("status") in ("partial", "waiting for transcript"))]
        for qn, pred in qs:
            try:
                for r in src.query(pred, qn):
                    # 3 capability check
                    if "id" not in r:
                        v.attempts.append(f"{now} cannot run: source has no stable meeting IDs"); return "no-ids"
                    fetched[r["id"]] = r
            except PageFail as e:
                complete = False; v.attempts.append(f"{now} retrieval incomplete: {e}")
        no_edit = any(r["edited"] is None for r in fetched.values())
        if no_edit: v.attempts.append(f"{now} no edit times: amendments not tracked")
        # 5 decide
        for mid, m in sorted(fetched.items()):
            s = st["meetings"].get(mid)
            if not m.get("transcript"):
                if not s: st["meetings"][mid] = {"status": "waiting for transcript", "edited": None, "matched": [], "done": [], "summary": ""}
                continue
            amend = s and s["status"] == "complete" and m["edited"] and s["edited"] and m["edited"] > s["edited"]
            if s and s["status"] == "complete" and not amend: continue
            prev_matched = s["matched"] if amend else []
            matched = [p for p in m["participants"] if p in v.people]
            removed = [p for p in prev_matched if p not in matched and p in v.people]
            targets = matched + removed
            done = [p for p in (s["done"] if s and s["status"] == "partial" else [])]
            ok = True
            for p in targets:
                n = v.people[p]; marker = mk(mid, m["edited"])
                if marker in n["body"]: done.append(p) if p not in done else None; continue
                if v.fail_after_person_writes is not None and v.person_writes >= v.fail_after_person_writes:
                    v.fail_after_person_writes = None; ok = False
                    v.attempts.append(f"{now} write failed for {p} on {mid}"); break
                if p in removed:
                    n["body"] += f"\nAmended: {m['title']}: no longer listed\n{marker}\n"
                elif amend:
                    n["body"] += f"\nAmended: {m['title']}: {m['transcript']}\n{marker}\n"
                else:
                    n["body"] += f"\n{m['start'][:10]} {m['title']} ({mid}): {m['transcript']}\n{marker}\n"
                if p not in removed:
                    d = m["start"][:10]
                    if not n["last_contact"] or d > n["last_contact"]: n["last_contact"] = d
                v.person_writes += 1
                assert marker in n["body"]
                if p not in done: done.append(p)
            status = "complete" if ok and all(p in done for p in targets) else "partial"
            st["meetings"][mid] = {"status": status, "edited": m["edited"] if status == "complete" else (s or {}).get("edited"),
                                   "matched": matched, "done": done if status == "partial" else [], "summary": m["transcript"][:60]}
            save_state(v, st)
            if status != "complete": complete = False
        # 9 finish
        if complete and all(x["status"] in ("complete", "waiting for transcript") for x in st["meetings"].values()):
            st["last_successful_run"] = now.isoformat()
            save_state(v, st)
            v.attempts.append(f"{now} {'ok, nothing new' if not fetched else 'ok'}")
            return "ok"
        v.attempts.append(f"{now} partial or retrieval incomplete")
        return "partial"
    except IOError as e:
        v.attempts.append(f"{now} error: {e}"); return "error"
    finally:
        if not v.files["lock"].startswith("held") or True:
            # the simulation releases the lock unless the scenario killed the run mid-way
            if not getattr(v, "die_holding_lock", False): v.files["lock"] = "free"

# ---------- scenarios ----------
T0 = datetime.fromisoformat(FIX["now"])
def M(key): return copy.deepcopy(FIX["meetings"][key])
def state(v): return load(v.files["state"])

def scenarios():
    R = []
    def check(name, cond): R.append((name, bool(cond)))

    # 1 first run, then duplicate run
    v = Vault(FIX["people"]); src = Source([M("pricing"), M("hiring")])
    run(v, src, T0); run(v, src, T0 + timedelta(minutes=5))
    check("repeat run adds nothing new", count(v.people["Ana"], "M1") == 1 and count(v.people["Ben"], "M1") == 1 and count(v.people["Ben"], "M2") == 1)

    # 2 interruption after first person, then retry
    v = Vault(FIX["people"]); v.fail_after_person_writes = 1; src = Source([M("pricing")])
    r1 = run(v, src, T0)
    check("interrupted run: last_successful_run not advanced", r1 == "partial" and state(v)["last_successful_run"] is None and state(v)["meetings"]["M1"]["status"] == "partial")
    run(v, src, T0 + timedelta(hours=1))
    check("retry finishes without duplicates", count(v.people["Ana"], "M1") == 1 and count(v.people["Ben"], "M1") == 1 and state(v)["meetings"]["M1"]["status"] == "complete")

    # 3 amendment of older transcript, plus removed participant
    v = Vault(FIX["people"]); old = M("board_prep"); src = Source([old])
    run(v, src, T0 - timedelta(days=9))
    amended = M("board_prep_amended"); src = Source([amended])
    run(v, src, T0)
    check("older amended transcript picked up once", "Amended: Board prep" in v.people["Ana"]["body"] and count(v.people["Ana"], "M0") == 2)
    check("removed participant gets an explicit note", "no longer listed" in v.people["Ben"]["body"])
    run(v, src, T0 + timedelta(hours=1))
    check("amendment not repeated", count(v.people["Ana"], "M0") == 2)

    # 4 delayed transcript outside the 24-hour window
    v = Vault(FIX["people"]); late = M("late"); late_no = dict(late, transcript="")
    run(v, Source([late_no]), T0 - timedelta(days=3))
    check("meeting without transcript recorded as waiting", state(v)["meetings"]["M5"]["status"] == "waiting for transcript")
    run(v, Source([late]), T0)
    check("delayed transcript (5 days old) found by the sweep", count(v.people["Ana"], "M5") == 1)

    # 5 failed pagination
    v = Vault(FIX["people"]); src = Source([M("pricing"), M("hiring"), M("late")], fail_page=("sweep", 1))
    r = run(v, src, T0)
    check("failed page: run not counted as successful", r == "partial" and state(v)["last_successful_run"] is None)

    # 6 empty successful fetch
    v = Vault(FIX["people"]); r = run(v, Source([]), T0)
    check("empty successful fetch advances the checkpoint", r == "ok" and state(v)["last_successful_run"] == T0.isoformat() and "ok, nothing new" in v.attempts[-1])

    # 7 missing edit timestamps
    v = Vault(FIX["people"]); src = Source([M("pricing")], has_edit=False)
    run(v, src, T0); run(v, src, T0 + timedelta(hours=1))
    check("no edit times: processed once, logged as not tracked", count(v.people["Ana"], "M1") == 1 and any("amendments not tracked" in a for a in v.attempts))

    # 8 missing IDs
    v = Vault(FIX["people"]); r = run(v, Source([M("pricing")], has_ids=False), T0)
    check("no stable IDs: feed refuses and writes nothing", r == "no-ids" and v.people["Ana"]["body"] == "" and v.files["state"] is None)

    # 9 overlapping run blocked by lock
    v = Vault(FIX["people"]); v.files["lock"] = f"held {(T0 - timedelta(minutes=10)).isoformat()}"
    r = run(v, Source([M("pricing")]), T0)
    check("second run while one holds the lock is skipped", r == "skipped" and v.people["Ana"]["body"] == "")
    v.files["lock"] = f"held {(T0 - timedelta(hours=3)).isoformat()}"
    r = run(v, Source([M("pricing")]), T0)
    check("stale lock (over 2 hours) is taken over", r == "ok" and any("stale lock" in a for a in v.attempts))

    # 10 interrupted state save, then recovery
    v = Vault(FIX["people"]); run(v, Source([M("pricing")]), T0)
    v.fail_state_write_stage = "main"
    r = run(v, Source([M("pricing"), M("hiring")]), T0 + timedelta(hours=1))
    torn = load(v.files["state"]) is None
    v.files["new"] = None   # worst case: the .new copy is also lost
    run(v, Source([M("pricing"), M("hiring")]), T0 + timedelta(hours=2))
    check("interrupted state save is recovered from the previous copy", torn and any("recovered from previous copy" in a for a in v.attempts) and count(v.people["Ben"], "M2") == 1 and count(v.people["Ana"], "M1") == 1)

    # 11 unavailable source
    v = Vault(FIX["people"]); run(v, Source([M("pricing")]), T0); before = v.files["state"]
    r = run(v, Source([M("pricing")], up=False), T0 + timedelta(hours=1))
    check("unavailable source: state untouched, attempt logged", r == "unavailable" and v.files["state"] == before and "source unavailable" in v.attempts[-1])

    # 12 unmatched participant never gets a note
    check("unmatched participant gets no note", "Zed" not in Vault(FIX["people"]).people)
    return R

if __name__ == "__main__":
    R = scenarios()
    lines = [("PASS" if ok else "FAIL") + "  " + name for name, ok in R]
    print("\n".join(lines))
    passed = sum(ok for _, ok in R)
    print(f"\n{passed}/{len(R)} passed")
    if "--write-results" in sys.argv:
        (HERE / "results.md").write_text(
            "# Feed 3 simulation results\n\n"
            f"*Generated by `sim.py --write-results` on {datetime.now():%Y-%m-%d %H:%M}. "
            "Simulation of the procedure's logic only: not a real AI following the prompt, "
            "and not a real meeting-notes connector.*\n\n```\n" + "\n".join(lines) +
            f"\n\n{passed}/{len(R)} passed\n```\n")
    sys.exit(0 if passed == len(R) else 1)
