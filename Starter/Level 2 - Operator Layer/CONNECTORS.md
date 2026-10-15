# Connectors Map

*The one place that says, for every external system you use: what truth lives there, how an agent reaches it, whether it may read or write, and where the credentials live. The agent reads this before touching any external system. If a tool isn't on the map, the agent asks before using it.*

*This is not a credential store. No keys, passwords, or account numbers in this file, ever. It points at where they live.*

---

## Standing rules

1. **Read-only by default.** Any write (send, post, publish, import, tag, schedule, edit a live page, change a setting) needs your explicit approval in the conversation. Describing a problem is not approval. Feeds write only what their prompt names.
2. **Reversibility is the line.** Drafting, filing, tagging in the vault, research, preparing: the agent runs these unattended. Anything the outside world sees, anything that moves money, anything that can't be undone: it parks for your approval.
3. **Money systems are human-only.** No agent logs in to, enters credentials for, or moves funds on any bank, brokerage, or payment account. Their data enters the vault through documents you produce.
4. **Prefer a connector when one exists and works.** Fall back to a logged-in browser when it doesn't. The agent never signs in and never enters a credential.
5. **Secrets never live in the vault.** This folder syncs (Dropbox, iCloud) and may be committed to git, so a key written here is a key in every synced copy and in git history forever. Keys, passwords, and tokens live in your password manager, your OS keychain, or an environment variable on the machine that runs the agent. A project `CONTEXT.md` holds account IDs, portal URLs, and a pointer ("API key: password manager item 'Email platform API'"), never the value. If a key is ever pasted into a vault file by mistake, rotate it; deleting the line doesn't remove it from history.
6. **Sensitive folders stay closed.** Health records, client notes, anything with a confidentiality clause: named here, never quoted outside its folder. A personal vault is never read by a company vault's shared feeds.

## Access paths

| Path | Meaning |
|---|---|
| Connector | A native integration (MCP connector in Claude, a plugin, an API the agent can call directly). Fast, precise, permission-gated. |
| Browser | The agent driving your logged-in browser. Needs an existing login. |
| Local | Files on disk: your synced folder, exports, this vault. |
| Human | You do it. The agent prepares; you execute. |

---

## The map

Group rows by area of your life or work. One row per system. Delete the examples once you have real rows.

### [Area 1, e.g. Marketing and sales]

| Tool | Truth that lives there | Access | Read / Write | Credentials live in | Used by |
|---|---|---|---|---|---|
| [Email platform] | Subscribers, campaigns, automations. The source of truth for leads. | Connector | Read freely. Sends and automation edits need approval. | Password manager item "[name]"; account and list IDs in `1. Projects/[project]/CONTEXT.md` | [project], [feed] |
| [CRM] | Pipeline and deal stages. Not a reporting source if the data is stale; say so here. | Connector | Read. Updates with approval. | Connector login | [project] |
| [Website CMS] | Live pages, forms, redirects. Page IDs worth listing. | Browser, logged in | Read. Any live change needs approval; draft in files first. | Browser login | [project] |
| [Analytics] | Traffic and events. Note what it is *not* reliable for (e.g. purchases). | Browser | Read only | Browser login | [daily feed] |

### [Area 2, e.g. Finance and operations]

| Tool | Truth that lives there | Access | Read / Write | Credentials live in | Used by |
|---|---|---|---|---|---|
| [Accounting] | The books: cash, P&L, invoices | Connector | Read only. No entries from an agent. | Connector login | [weekly financials feed] |
| [Bank, brokerage] | Balances | **Human only** | Never | You | Data enters via documents you file |

### [Area 3, e.g. Knowledge and capture]

| Tool | Truth that lives there | Access | Read / Write | Credentials live in | Used by |
|---|---|---|---|---|---|
| [Sync: Dropbox, iCloud, git] | The vault itself | Local | Read and write inside each folder's rules | Your login | Everything |
| [Meeting recorder] | Transcripts and participant names (the verified source for spelling) | Connector | Read only | Connector login | People feed |
| [Email] | Threads and drafts | Connector | Read, search, draft. **Send only with approval, per message.** | Connector login | Morning feed, outreach |
| [Calendar] | Your schedule | Connector | Read. Create or change events with approval | Connector login | Weekly plan |
| [Task manager] | Project ranking the weekly plan follows | Human or connector | State which | App | Weekly plan |
| Scheduled feeds | The standing automations (`seat/feeds.md`) | Local task definitions | Read. Create or edit with approval (they're configuration) | n/a | See the list |

### [Area 4, e.g. Health]

| Tool | Truth that lives there | Access | Read / Write | Credentials live in | Used by |
|---|---|---|---|---|---|
| [Health export] | Personal health data. **PII: never quoted outside its folder.** | Local | Read for you only | n/a | [dashboard feed] |

### Company vault (fill in when this seat joins one)

| Tool | Truth that lives there | Access | Read / Write | Credentials live in | Used by |
|---|---|---|---|---|---|
| [Shared vault path] | The company's memory and seats. Pointer lives in `seat/seat.md`. | Local (shared drive or git) | Per the company vault's own CONNECTORS.md | n/a | Company tasks only; never reads this personal vault |

---

## Credential sprawl (fix list)

List every place a credential is duplicated, and the plan to get it to one home. The agent adds to this list when it finds a copy.

- [ ] [Example: API key pasted into `CONTEXT.md` and embedded in two feed prompts. Rotate the key, move it to the password manager, leave a pointer in CONTEXT.md, and have the prompts reference the pointer.]

## Open questions

Rows the agent couldn't verify. Answer, then delete.

- [ ] [Which task manager is live?]
- [ ] [Is the git repo local-only or pushed to a remote? If a remote, does any committed file hold a key?]

## Maintenance

- Adding a connector, a feed that touches a new system, or a new credential location: add the row the same day. This file is not rebuilt automatically.
- Project `CONTEXT.md` files keep account IDs and credential pointers for their own systems. This file points at them; it doesn't duplicate them. Neither file holds a secret value.
- `knowledge/agents.md` tells the agent to read this file before touching any external system.
