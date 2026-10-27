# ATS check: companies/google-backend/resume.pdf vs google-backend

Extracted with `pdftotext resume.pdf -` on this device. First lines the software reads:

```
Riya Sharma
Pune, India · riya.sharma@example.com · +91 90000 00000 · linkedin.com/in/riya-sharma-demo
SUMMARY
Backend engineer with 2.5 years building Java and Spring Boot payment services: event-driven flows on
```

| Check | Result | Proof (from the extracted text) |
|---|---|---|
| Contact | PASS | Name on line 1, email and phone on line 2, plain text |
| Headings | PASS | SUMMARY, EXPERIENCE, PROJECTS, SKILLS, EDUCATION, each followed by its own content |
| Dates | PASS | `Jul 2023 – Present`, `Jan 2023 – Jun 2023` on the role lines; `2023` on the degree line |
| Order | PASS | Reads top to bottom in the order shown |
| Keywords | PASS | Java, distributed services, RabbitMQ, Kubernetes (EKS), REST APIs, MySQL, Redis, on-call, JUnit, integration tests, design doc, code review |
| Readable text | PASS | No images, icons or skill bars |

Not added on purpose (user said no in questions.md): Go, gRPC, Kafka.

No changes needed.
