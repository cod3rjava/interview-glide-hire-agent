---
name: ats-check
description: Check what resume software (an ATS) can actually read from a resume, against one job description. Extracts the plain text on the user's device, checks contact line, headings, dates, reading order and the job's keywords, writes a report, and makes an ATS-friendly one-column version if anything fails. Use before applying, after resume-tailor or on any resume.
---

# ATS check

Before a recruiter sees a resume, the application software usually turns it into plain text. Two columns, icons, tables and text boxes can come out in the wrong order or not at all. This skill shows the user what the software sees, and fixes it.

## Inputs
- The resume to check. Default: `companies/<job>/resume.pdf` (made by `resume-tailor`). The user can name another file, e.g. `my-resume/resume.pdf`.
- `companies/<job>/jd.md`: the job description.
- `companies/<job>/questions.md` (if it exists): skills the user confirmed or denied. Use it for the keyword check.

## Steps
1. **Extract the plain text, on the device**, in reading order:
   `pdftotext <resume.pdf> -` (do NOT use `-layout`: it hides column problems).
   DOCX: `textutil -convert txt -stdout <file>` (macOS) or `pandoc <file> -t plain`.
   No `pdftotext`? It's free: `brew install poppler` / `sudo apt install poppler-utils` / Xpdf tools on Windows. Ask before installing.
   Show the user the first ~25 lines of the extracted text: this is what the robot sees.
2. **Check**, each as PASS or FIX:
   - **Contact**: name, email and phone are in the first 5 lines, as plain text (no icons like ✆ ✉ standing in for words).
   - **Headings**: standard names (Summary, Experience, Projects, Skills, Education), and each heading is directly followed by its own content (not by another heading or by text from a side column).
   - **Dates**: every job and degree has a readable date range next to it (`Jul 2023 – Present`).
   - **Order**: the text reads in the same order a person sees it. Side-column text mixed into the main column = FIX.
   - **Keywords**: the job's must-have skills (from jd.md) that the user has (resume or `questions.md`) appear in the text, in the JD's words. A must-have the user said **no** to is not a FIX; it stays out.
   - **Readable text**: no text inside images, no skill bars or star ratings carrying meaning (the software drops them).
3. **Write** `companies/<job>/ats-report.md`: one line per check with PASS/FIX, the exact broken lines quoted from the extracted text, and the simplest fix. If you checked a file that is not the job's resume, name the report `ats-report-<file-name>.md`.
4. **If anything is FIX, make the ATS-friendly version**:
   - If `companies/<job>/resume.md` exists (from `resume-tailor`), fix it there.
   - If not, write `companies/<job>/resume.md` from the checked resume's content only, in the `resume-tailor` format (one column, standard headings, plain contact line, dates on the role line). Move nothing in or out except fixing layout; never add skills or numbers.
   - Export: `python3 scripts/export.py companies/<job>/resume.md`, then run step 1-2 again on the new PDF to prove it passes.
5. **Tell the user** in 5 lines or fewer: which checks failed and why, what you changed, and the result of the re-check.

## Rules
- Never add a skill, tool or number the user hasn't confirmed, even if the JD wants it.
- Never upload the resume to an online "ATS checker". Everything runs on the user's device.
- No made-up "ATS score" percentages. Report the checks, with the lines that prove them.
