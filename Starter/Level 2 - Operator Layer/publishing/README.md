# publishing/

Tools for producing the kit's shareable files. Not part of running the system; a person using the Starter never needs this folder.

## build_cheat_sheet.py

Regenerates `Cheat Sheet - Operator's Seat.pdf`, the one-page card of the seven steps.

Needs `reportlab`. On a Mac, the system Python refuses `pip install`, so use a small private environment: `python3 -m venv ~/.venvs/opseat`, then `~/.venvs/opseat/bin/pip install reportlab pypdf`, and run the script with `~/.venvs/opseat/bin/python`. `pypdf` is optional: with it installed, the script checks the page count and exits with an error if the sheet runs past one page; without it, the script says the check was skipped, and you open the PDF to confirm.

By default the PDF is written to the kit's top folder (the script walks up from its own location to the folder that holds `START HERE.md`), whatever directory you run it from. Use full paths:

```
python3 "/full/path/to/Starter/Level 2 - Operator Layer/publishing/build_cheat_sheet.py"
python3 "/full/path/to/.../build_cheat_sheet.py" --body-size 10      # smaller body text if it spills to two pages
python3 "/full/path/to/.../build_cheat_sheet.py" --out ~/Desktop/sheet.pdf
```

Keep the steps in the script identical to the seven steps in `START HERE.md`; the sheet is the summary, not a second version.
