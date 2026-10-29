# LinkedIn profile: google-backend
> Sample run of `linkedin-profile`. Riya is a made-up person and the JD is a sample. Copy these into LinkedIn yourself: Edit profile → Headline / About / Skills. Nothing was posted.

Sources: `resume.md` (this folder), `jd.md`, `questions.md`, `examples/my-linkedin.md` (before).

## Headline
Backend Engineer | Java, Spring Boot, Kubernetes | Distributed payment services, event-driven pipelines, on-call

## About
I'm a backend engineer with 2.5 years building Java and Spring Boot payment services.

At Finlytics I built the payment reconciliation flow across 3 distributed services, with retries and idempotency so no payment is applied twice. I run event-driven pipelines on RabbitMQ, moved 3 services to Kubernetes (EKS), and I'm on call one week a month.

Next, I want a backend role on large distributed systems, where reliability, testing and clean design matter.

## Top skills
1. Java
2. Distributed systems
3. Kubernetes
4. REST APIs
5. SQL

## What changed and why
- Headline: "Software Developer | Open to work" → "Backend Engineer | Java, Spring Boot, Kubernetes | …". The JD is a backend role; the resume summary says backend engineer, Java, Spring Boot, Kubernetes.
- About: the generic line ("hardworking and passionate… reputed organization") → what she built, from the resume's experience bullets. Numbers (2.5 years, 3 services) are from the resume.
- Kubernetes: added. Confirmed in questions.md (#1: moved 3 payment services to EKS).
- Distributed systems: added. Confirmed in questions.md (#5: reconciliation flow across 3 services).
- REST APIs, SQL: added. In the resume's Skills, and minimum qualifications in the JD.
- MySQL → SQL (the JD's word). Teamwork → removed (not a skill recruiters search for; code reviews are in the About instead).

## Left out
- Go: denied in questions.md (#4).
- gRPC / Protocol Buffers: denied (#2).
- Kafka / Pub/Sub: denied (#3). RabbitMQ is used instead, in the About.
