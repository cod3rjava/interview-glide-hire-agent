---
name: linkedin-profile
description: Rewrite the user's LinkedIn headline, About section and top skills for one target job, using only what is true in their resume (and what they confirmed in questions.md). Writes companies/<job>/linkedin.md for the user to copy in themselves. Never logs in, never posts. Use after resume-tailor, or whenever the resume and the LinkedIn profile say different things.
---

# LinkedIn profile

Recruiters check LinkedIn after (or before) the resume. If the resume says "Backend engineer" and LinkedIn still says "Software Developer | Open to work", the story doesn't match. This skill makes the profile tell the same story as the tailored resume, for the job the user wants.

## Inputs
- The resume: `companies/<job>/resume.md` (made by `resume-tailor`) if it exists, else the file in `my-resume/`.
- `companies/<job>/jd.md`: the job the user wants. Its words decide which true skills go first.
- `companies/<job>/questions.md` (if it exists): skills the user confirmed or denied. Confirmed = allowed. Denied = never.
- Optional `my-linkedin.md` (repo root, or `examples/my-linkedin.md` for the sample): the user pastes their current headline, About and skills. If it's missing, ask for them once; if the user skips, write the new profile without a before/after.

## Steps
1. **Read** the resume, the JD and questions.md. List the JD's must-have and preferred skills, and mark each: in the resume / confirmed in questions.md / denied / not mentioned.
2. **Headline** (max 220 characters): the target role in the JD's words + 2-3 true strengths from the resume. No "Open to work", no "Aspiring", no emojis, no company names the user didn't work for.
3. **About** (3 short paragraphs, first person, max ~120 words):
   - what you do and for how long (from the resume summary),
   - what you've actually built, in plain words (from the experience bullets; numbers only if the resume has them),
   - what you're looking for next (the JD's kind of role, no company name).
   No clichés: "passionate", "hardworking", "go-getter", "results-driven", "team player", "reputed organization".
4. **Top 5 skills**: skills the user really has, in the JD's words and the JD's order of importance. A skill is allowed only if it's in the resume or confirmed in questions.md. A JD skill the user denied stays out, even if it would help.
5. **Write** `companies/<job>/linkedin.md`:
   - `## Headline`, `## About`, `## Top skills` (the new text, ready to copy),
   - `## What changed and why`: one line per change (old → new, and the resume line or question that allows it),
   - `## Left out`: JD skills not used, and why (denied / not in resume).
6. **Tell the user** in 3 lines: the new headline, the skills added and left out, and: "Copy these into LinkedIn yourself: Edit profile → Headline / About / Skills."

## Rules
- Never invent a skill, title, employer, number or certification. Only the resume and questions.md count as proof.
- Never log in to LinkedIn, never scrape it, never post or change anything there. The user copies the text in.
- Don't promise results ("get hired faster"). Just make the profile match the resume.
