# ATS check: my-resume/resume.pdf (sample, two-column original) vs google-backend

Extracted with `pdftotext resume.pdf -` on this device. First lines the software reads:

```
Riya
Sharma
PROFILE
Software Developer
Hardworking and passionate software developer with 2+ years of
...
CONTACT
WORK EXPERIENCE
✆ +91 90000 00000
✉ riya.sharma@example.com
```

| Check | Result | Proof (from the extracted text) | Fix |
|---|---|---|---|
| Contact | FIX | Phone and email come after the profile and after the WORK EXPERIENCE heading (lines 16-17); they start with icons `✆` `✉` | One plain contact line under the name |
| Headings | FIX | `CONTACT` is followed by `WORK EXPERIENCE`, then the phone number. `EDUCATION` is followed by `LANGUAGES` and `HOBBIES` before the degree | One column, each heading followed by its own content |
| Dates | PASS | `Jul 2023 – Present`, `Jan 2023 – Jun 2023`, `2023` are readable | — |
| Order | FIX | Side-column text (contact, skills, languages) is mixed into the main column | One column |
| Keywords | FIX | Confirmed in questions.md but missing: Kubernetes, distributed systems, on-call, integration tests (JUnit) | Add them in the JD's words where true |
| Readable text | FIX | Skill bars carry the skill level; they are dropped | Remove bars; list skills as text |

Denied in questions.md and correctly absent: Go, gRPC, Kafka.

Fixed version: `resume.md` → `resume.pdf` / `resume.docx` in this folder (one column, made by resume-tailor on Day 1). Re-check of that file: `ats-report.md` (all PASS).
