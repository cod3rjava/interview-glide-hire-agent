---
name: resume-tailor
description: Rewrite the user's resume for one specific job description, honestly. Reads my-resume/ and companies/<job>/jd.md, asks about skills the job wants that the resume never mentions, then writes resume.md, resume.docx and resume.pdf into that company folder. Use when the user wants their resume tailored to a job.
---

# Resume tailor

Make one resume per job. Same person, same truth, written in the job's language.

## Inputs
- `my-resume/`: the user's current resume (`.pdf`, `.docx`, `.md` or `.txt`). If there are several, use the newest.
- `companies/<job>/jd.md`: the job description, pasted by the user.
  If the user names a job folder, use it. If not, list the folders in `companies/` and ask which one.
- `companies/<job>/questions.md` (if it exists): answers from an earlier run. Do not ask these again.

## Steps
1. **Read** the resume and the JD.
2. **Pull out what the job wants**: must-have skills, tools, and the key phrases the JD repeats. Also note the role level and what the team does.
3. **Find the gaps**: every must-have the resume never mentions.
4. **Ask before adding.** For each gap, ask the user: "The job wants **X**. Have you used it? Where, and what did you do?"
   Ask all gap questions in one message. Wait for the answers.
   Save the questions and the answers in `companies/<job>/questions.md`.
   If the user says no, leave it out. Never add it anyway.
5. **Rewrite the resume** for this job:
   - Summary: 2 lines that match the role, using the JD's words for things the user really did.
   - Put the most relevant experience and projects first. Cut or shorten what this job doesn't care about.
   - Bullets: action + what you built + result. Use the JD's terms where they are true ("event streaming with Kafka", not "messaging stuff").
   - If a bullet needs a number the resume doesn't have, ask for it. Never invent one.
   - Skills: list the JD's must-haves the user has first.
   - One page if the user has under 5 years of experience.
6. **Write** `companies/<job>/resume.md` in the format below.
7. **Export**: run `python3 scripts/export.py companies/<job>/resume.md`.
   This creates `resume.docx` and `resume.pdf` in the same folder.
8. **Tell the user** in 5 lines or fewer: what changed, which gaps were added (with their confirmation), which were left out, and the file paths.

## resume.md format
Keep exactly this structure so the export works:

```
# Full Name
City · email · phone · linkedin.com/in/... · github.com/...

## Summary
Two lines.

## Experience
### Role | Company | Mon YYYY – Mon YYYY
- Bullet with **bold** only for key tech.

## Projects
### Project name | Tech, tech
- Bullet.

## Skills
- Languages: ...
- Backend: ...

## Education
### Degree | College | YYYY
```

## Rules
- Never invent experience, employers, dates, numbers, or tools. Only what is in the resume or what the user confirmed.
- Keep the user's voice. Don't stuff keywords into sentences that stop making sense.
- The resume stays on the user's device. Don't upload it anywhere or paste it into other tools.
- Don't apply to the job. This skill only writes files.
