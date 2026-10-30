---
name: job-finder
description: Turn the user's target role and city into ready-to-use job searches (LinkedIn Jobs + Google site: queries for company career pages and job boards). After the user pastes the listings they found, rank each one High / Medium / Low against their resume with a one-line reason (must-haves matched and missing), and make a companies/<job>/jd.md folder for every job worth applying to. Never scrapes, never logs in, never applies. Use before resume-tailor, when the user doesn't know which jobs to go for.
---

# Job finder

Applying to every job you see burns the week, and most of those jobs never fit. This skill finds the ones that do, so the user only tailors a resume for those.

The agent does **not** search the web or log in anywhere. It writes the searches; the user runs them and pastes what they find.

## Inputs
- The resume: the file in `my-resume/` (or `companies/<job>/resume.md` if one exists and the user says to use it).
- `my-search.md` (repo root; `examples/my-search.md` for the sample): target role, city (or remote), years of experience, must-haves, nice-to-haves, things to avoid. If it's missing, ask these 6 things once and save the answers there.
- Any `companies/*/questions.md`: skills the user already confirmed or denied in earlier skills. Confirmed counts as having it; denied counts as not having it.
- `job-search/listings.md`: the listings the user pasted (step 3). One `## ` heading per listing, then the text as copied (title, company, city, experience, requirements).

## Steps
1. **Read** the resume, `my-search.md` and every `questions.md`. Make the user's skill list: in the resume, confirmed, denied.
2. **Write the searches** to `job-search/searches.md` (3-6 of them), each ready to paste:
   - **LinkedIn Jobs**: the keywords for the search box (`"backend engineer" (Java OR "Spring Boot")`), the location, and which filters to set (date posted: past week; experience level matching their years).
   - **Company career pages**: Google queries with `site:` for the job-board systems companies use for their careers pages, e.g. `site:boards.greenhouse.io`, `site:jobs.lever.co`, `site:jobs.ashbyhq.com`, plus the role, a must-have skill and the city.
   - **One broad query** without `site:` that excludes what the user wants to avoid (`-senior -staff -lead` for 2-3 years of experience).
   Use the user's words for the role, plus the 1-2 common titles for the same work (Backend engineer / SDE / Java developer). Don't add skills the user doesn't have.
3. **Ask the user to paste** what they find into `job-search/listings.md`: "Run these, open the jobs that look right, and paste each listing under a `## ` heading. 5-15 is plenty." Wait for it. Never fetch the pages yourself.
4. **Rank each listing** against the user's skill list and `my-search.md`:
   - Pull out the listing's must-haves (required / minimum) and its experience range and city.
   - **High**: every must-have is in the resume or confirmed, the experience range fits, the city fits.
   - **Medium**: one must-have is missing or only a nice-to-have, or the role mixes in work the user hasn't done; still worth a look.
   - **Low**: a core must-have the user doesn't have (or denied), the experience is clearly above or below theirs, or it hits something in "avoid".
   - The reason is one line, in the listing's words: `Java ✓ · Spring Boot ✓ · Kubernetes ✓` / `needs Go ✕`. No percentages or scores: they look exact and aren't.
5. **Write** `job-search/ranked.md`: a table (listing, company, fit, reason) from High to Low, then for each Medium and Low one line on what would have to change (e.g. "only if you learn Go").
6. **Make job folders**: for every **High** listing (and Medium ones the user picks), create `companies/<slug>/jd.md` with the listing text exactly as pasted, plus a first line with where it came from (the URL or "pasted by the user"). Slug = `company-role` in lowercase with dashes. Don't overwrite a `jd.md` that exists.
7. **Tell the user** in 3 lines: how many High / Medium / Low, the folders made, and the next step: "run resume-tailor for <slug>" for each.

## Rules
- **No scraping, no login, no auto-apply.** The agent never opens job sites, never logs in to LinkedIn or a job board, never applies or messages a recruiter.
- **No invented skills.** Rank with what the resume and questions.md prove. A listing skill the user denied is a ✕, even if it's close.
- **No promises.** Don't say a job is a sure thing or guess the chance of getting it. High fit means "worth tailoring for", nothing more.
- Keep the user's search and listings on their device (`job-search/` is in `.gitignore`).
