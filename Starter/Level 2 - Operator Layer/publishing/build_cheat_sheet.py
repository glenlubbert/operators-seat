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
"""Build the one-page Operator's Seat cheat sheet PDF.

Usage:
    python3 build_cheat_sheet.py [--out PATH] [--body-size N]

--out        where to write the PDF. Default: the kit's top folder, found by
             walking up from this script to the folder that contains "START HERE.md".
--body-size  body text size in points (default 11). Lower it if the sheet spills
             to a second page.

Needs reportlab. pypdf is optional: if installed, the script checks the page
count and exits with an error when the sheet is longer than one page.
"""
import argparse, sys
from pathlib import Path
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib import colors
ap=argparse.ArgumentParser()
ap.add_argument("--out")
ap.add_argument("--body-size",type=float,default=11.0)
args=ap.parse_args()
def kit_root():
    for d in Path(__file__).resolve().parents:
        if (d/"START HERE.md").exists(): return d
    return Path.cwd()
out=str(Path(args.out) if args.out else kit_root()/"Cheat Sheet - Operator's Seat.pdf")
BS=args.body_size
doc=SimpleDocTemplate(out,pagesize=letter,leftMargin=1.0*inch,rightMargin=1.0*inch,topMargin=0.6*inch,bottomMargin=0.5*inch)
NAVY=colors.HexColor('#152A3A'); GREY=colors.HexColor('#666666'); CORAL=colors.HexColor('#EB5931')
H=ParagraphStyle('h',fontName='Helvetica-Bold',fontSize=26,leading=30,textColor=NAVY,spaceAfter=4)
Sub=ParagraphStyle('s',fontName='Helvetica',fontSize=12,leading=16,textColor=GREY,spaceAfter=18)
Num=ParagraphStyle('n',fontName='Helvetica-Bold',fontSize=26,leading=28,textColor=CORAL,alignment=1)
T=ParagraphStyle('t',fontName='Helvetica-Bold',fontSize=12.5,leading=16,textColor=NAVY)
B=ParagraphStyle('b',fontName='Helvetica',fontSize=BS,leading=BS*1.36)
Mono=ParagraphStyle('m',fontName='Courier',fontSize=10.5,leading=15)
End=ParagraphStyle('e',fontName='Helvetica-Bold',fontSize=12.5,leading=16,textColor=NAVY,spaceBefore=6)
Foot=ParagraphStyle('f',fontName='Helvetica-Oblique',fontSize=9.5,leading=13,textColor=GREY)

steps=[
 ("Copy the folders and let it interview you.","Unzip, copy Starter, rename it. Attach it as a project (Claude: Projects, +, Use an existing folder. ChatGPT: Work, project, Add folder). Type \"Read AGENTS.md, then interview me.\" About half an hour."),
 ("Catch it being wrong.","New conversation. Ask: \"What should I be careful about this week?\" Correct what it misses. If it doesn't offer to save, say \"Save that to [your folder].\""),
 ("Tell it five true things.","Say: \"Here are some things that are true about my work. File them in [your folder].\" Or drop files in 0. Inbox and say \"Sort my inbox.\" Then ask something only those facts answer."),
 ("Fill in one project.","Step 1 made a folder for each project you named. Say: \"Let's fill in [project name].\" New conversation: ask what's due."),
 ("Give it one rule.","Something you've corrected twice, or anything you always want. Say: \"From now on, [the rule]. Make that a rule in [your folder].\" Then: \"Show me the line and the file it's in.\""),
 ("Do the Friday audit together.","Whatever day it is, once now. Say: \"Run the Friday audit.\" Approve what it saves. Then: \"Put fifteen minutes on my calendar every Friday for this.\""),
 ("Run the first feed, then schedule it.","Say: \"Run the first feed.\" Read what it found. If it's useful: \"Schedule that for Friday mornings.\""),
]
rows=[]
for i,(t,b) in enumerate(steps,1):
    rows.append([Paragraph(str(i),Num),[Paragraph(t,T),Paragraph(b,B)]])
tbl=Table(rows,colWidths=[0.7*inch,5.8*inch])
tbl.setStyle(TableStyle([('VALIGN',(0,0),(-1,-1),'TOP'),('TOPPADDING',(0,0),(-1,-1),6),('BOTTOMPADDING',(0,0),(-1,-1),6),('LEFTPADDING',(0,0),(-1,-1),4),('LINEBELOW',(0,0),(-1,-2),0.4,colors.HexColor('#dddddd'))]))

story=[Paragraph("Operator's Seat",H),
       Paragraph("An AI chief of staff for you and your business, built for privacy and portability. Seven steps, in order: one a day or back-to-back.",Sub),
       tbl, Spacer(1,14),
       Paragraph("That's it.",End),
       Paragraph("Seven steps. One habit. You never opened a file, and you made every decision. The AI files as you go; you do Fridays. Skip Fridays and it rots in about six weeks.",B),
       Spacer(1,16),
       Paragraph("Switching AIs: attach the same folders in the other app and say \"Read AGENTS.md first.\" No second interview. The folders are yours, not any one AI's.",Foot),
       Spacer(1,6),
       Paragraph("Operator's Seat v0.9, October 2026. START HERE.md has the full seven steps; Why it works.md has the reasoning. Reuse terms: see REUSE.md.",Foot)]
doc.build(story)
print("wrote", out)
try:
    import pypdf
except ImportError:
    print("pypdf not installed; page count not checked. Open the PDF and confirm it is one page.")
    sys.exit(0)
n=len(pypdf.PdfReader(out).pages); print(n,"page(s)")
sys.exit(0 if n==1 else 1)
