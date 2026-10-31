# interview-glide-hire-agent

An open-source AI agent for your whole job hunt: **Resume → Job search → Outreach → Interview**.
Built in public, one new skill a day, by [InterviewGlide](https://interviewglide.com).

It's just text files: skills your AI already knows how to follow. No server, no account, no upload.

## How to use
1. Clone this repo and open it in Claude Code, Codex, Cursor, or any agent that reads `AGENTS.md`.
2. Put your resume (PDF, DOCX or MD) in `my-resume/`.
3. Make a folder for the job, e.g. `companies/google-backend/`, and paste the job description into `jd.md`.
4. Not sure which jobs? Ask **"run job-finder"** first: it writes the searches and makes the job folders for you.
5. Ask: **"run resume-tailor for google-backend"**, then **"run ats-check for google-backend"** and **"run linkedin-profile for google-backend"**.
6. Before you apply or interview: **"run company-brief for google-backend"**.

Using ChatGPT or another chat app? Open a skill's `SKILL.md`, paste it in with your resume and the JD.

`my-resume/` and `companies/` are in `.gitignore`, so your files stay on your device.

## Skills
| Day | Skill | What it does |
|---|---|---|
| 1 | [`resume-tailor`](skills/resume-tailor/SKILL.md) | Rewrites your resume for one JD, asks before adding anything, saves `resume.pdf` + `resume.docx` in the job folder |
| 2 | [`ats-check`](skills/ats-check/SKILL.md) | Shows what resume software reads from your PDF (plain text, on your device), checks contact, headings, dates, order and keywords, and makes a one-column version if anything fails |
| 3 | [`linkedin-profile`](skills/linkedin-profile/SKILL.md) | Rewrites your LinkedIn headline, About and top 5 skills for the job you want, from your resume only; saves `linkedin.md` for you to copy in (never logs in or posts) |
| 4 | [`job-finder`](skills/job-finder/SKILL.md) | Turns your role + city into LinkedIn and careers-page searches; you paste the listings, it ranks each High / Medium / Low with the reason and makes a job folder for the ones worth applying to (never scrapes, logs in or applies) |
| 5 | [`company-brief`](skills/company-brief/SKILL.md) | One-page brief per job: what the company builds, recent news, the team, what their interviews ask and questions to ask them; every line links to its source, anything not found stays blank |

New skill every day. Star the repo to follow along.

## Try it on the sample
`examples/` has a made-up person (Riya, 2.5 years Java backend) and a **sample** Google backend JD (not a real posting).
See `examples/companies/google-backend/` for the questions the agent asked and the resume it made, `examples/job-search/` for a job-finder run on 5 sample listings, and `examples/companies/google-backend/brief.md` for a company brief (real public sources).

Export a resume yourself: `python3 scripts/export.py companies/<job>/resume.md` (needs Python 3 and Chrome/Edge for the PDF; nothing to install).

## Rules the agent follows
1. **No lies.** It never invents experience, numbers or tools. It asks you, and only uses what you confirm.
2. **Stays on your device.** Your resume is never uploaded anywhere.
3. **You hit send.** It never applies or messages anyone for you. It drafts; you decide.

## Contributing
Found a better prompt or a bug? Open an issue or a PR. Each skill is one `skills/<name>/SKILL.md` file.

MIT License.
