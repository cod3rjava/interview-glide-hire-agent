# Company brief: Google · Software Engineer III, Backend (payments) · Bengaluru
> Sample run on the SAMPLE JD in `jd.md` (not a real Google posting). Riya is a made-up person. The company facts below are real and public, each with its link.

Sources checked: 2026-10-27

## 1. What they build
- Google Pay: Google's payment app; in India it is a UPI payments app, alongside Google Wallet for passes and tickets. [Deccan Herald](https://www.deccanherald.com/india/google-wallet-is-now-available-for-android-users-in-india-3013394)
- Google Pay is also how people pay in shops and online in other countries (tap to pay). [Google blog](https://blog.google/products-and-platforms/platforms/google-pay/tap-to-pay-google-pay-walmart/)

## 2. Recent news (last 12 months)
- **2026-08-21** · Tap to pay with Google Pay arrives at select Walmart and Sam's Club stores in the US. [Google blog](https://blog.google/products-and-platforms/platforms/google-pay/tap-to-pay-google-pay-walmart/)
- **2026-07-29** · India: "Ask Google Pay", a Gemini-powered assistant for questions about your spending (10 Indian languages), plus the Google Pay Flex SBI Card. [The Paypers](https://thepaypers.com/payments/news/google-pay-launches-ask-google-pay-and-sbi-flex-card) · [Fonearena](https://www.fonearena.com/blog/488504/google-payflex-sbi-card-ask-google-pay-ai-assistant.html/amp)
- **2025-11-19** · Philippines: more banks and card issuers to join Google Pay in 2026. [Philstar](https://www.philstar.com/business/2025/11/19/2488197/more-financial-institutions-join-google-pay-next-year/amp/)

## 3. The team
- From the SAMPLE JD: backend services behind payments in Google products, Java or Go, Pub/Sub or Kafka, Kubernetes, gRPC, on-call. (`jd.md`)
- Team size, manager, exact product area: **not found (no public source)**. Ask the recruiter which product this team owns.

## 4. What their interviews ask
- Official: Google's hiring page, [How we hire](https://www.google.com/about/careers/applications/how-we-hire/). **Could not read it (the page needs a browser).** Open it yourself and paste the steps here.
- Candidate reports, not official:
  - A recruiter screen, a coding phone screen, then a loop of several interviews; coding and data structures for this level, more system design for senior roles. [4dayweek.io guide](https://4dayweek.io/interview-process/google-software-engineer)
  - Google's former HR head described four things they look for: general cognitive ability, role-related knowledge, leadership, "Googleyness" (2015). [World Economic Forum](https://www.weforum.org/stories/2015/04/13-qualities-google-looks-for-in-job-candidates/)

## 5. Why this company, in your words (from your resume only)
- You build payment services already: the reconciliation flow with retries and idempotency at Finlytics maps to "backend services behind payments".
- You run event-driven payment pipelines (RabbitMQ, ~50k events a day) and on-call with a runbook: the JD asks for both.
- You don't have Go, gRPC or Kafka (`questions.md`): say you'd learn them, don't claim them.

## 6. Questions to ask them
1. Which part of payments does this team own: India UPI flows, cards, or the global Pay backend?
2. With Ask Google Pay reading spending data, how does the backend team work on privacy and reliability for AI features?
3. What does on-call look like for this team, and how is it shared?
