---
name: company-brief
description: Write a one-page brief for one job folder - what the company builds, recent news, the team you'd join, what their interviews ask, and questions to ask them - where every line links to its source and anything not found stays blank. Reads only public company information; never uploads the user's resume or details. Use after job-finder / resume-tailor, before outreach and interview prep.
---

# Company brief

"Why do you want to work here?" is hard to answer when all you know is the company's name. This skill makes one page the user can read in five minutes before applying, messaging someone, or walking into the interview.

## Inputs
- `companies/<job>/jd.md`: the company name, role, team and location come from here.
- The resume (`my-resume/` or `companies/<job>/resume.md`) and any `questions.md`: only for the "Why this company, in your words" section, and only on the user's device.

## Steps
1. **Read** `jd.md`. Write down: company, role, team (if the JD names it), city. If the company name isn't clear, ask the user.
2. **Look things up**, using the company name and the team/product only (never the user's name, resume or details):
   - The company's own pages first: about page, product pages, newsroom/blog, engineering blog, careers and hiring pages.
   - Then news sites for the last 12 months.
   - No web access? Write the list of pages and searches to `companies/<job>/brief-sources.md` ("open these and paste the text under each heading"), wait for the user, and use only what they paste.
3. **Write** `companies/<job>/brief.md`, one page, these sections:
   1. **What they build**: 2-3 lines on the business and products, from the company's own pages.
   2. **Recent news**: 3-5 items from the last 12 months, newest first. Each: date · one line · link. No item without a date and a link.
   3. **The team**: what this team does, from the JD and public pages (team or engineering blog, talks). Roles and products, not people: don't look up individual employees.
   4. **What their interviews ask**: rounds and what's tested, from the company's own hiring pages first. Anything from candidate reports (forums, review sites, guides) goes under "Candidate reports, not official" with its link.
   5. **Why this company, in your words**: 2-3 talking points that join the brief to the user's real experience (only what the resume or questions.md proves).
   6. **Questions to ask them**: 3 specific questions that come from the brief (a news item, the team's work, the interview process).
   Put `Sources checked: <date>` at the top.
4. **Mark the gaps.** Anything you can't find or can't read: `not found (no public source)` plus what to do ("ask the recruiter", "open the page yourself and paste it"). Never fill a gap with a guess.
5. **Tell the user** in 3 lines: the brief is in `companies/<job>/brief.md`, what was not found, and the next step (referral-message, cover letter or interview prep).

## Rules
- **Every fact has a source link.** A line without a link is your opinion: put it only in sections 5-6 and say so.
- **Nothing made up.** No guessed team sizes, salaries, tech stacks, funding or interview questions. Not found means blank.
- **Official vs rumour.** Interview info from anyone other than the company is labelled "candidate reports, not official".
- **Your details stay on your device.** Searches use the company name only; the resume is never uploaded or pasted anywhere.
- **Not about people.** No digging into individual employees or interviewers; that's for the user to do, if at all.
