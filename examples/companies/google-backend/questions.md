# Gap questions: google-backend
> Sample run. Riya is a made-up person; these answers are part of the demo.

The job wants things your resume never mentions. Have you used them? Where, and what did you do?

1. **Kubernetes**
   Yes. At Finlytics we moved 3 payment services to EKS last year. I wrote the Helm charts and the deploy pipeline in Jenkins.
2. **gRPC / Protocol Buffers**
   No. → left out
3. **Kafka or Pub/Sub**
   No Kafka. I use RabbitMQ for payment events, around 50k messages a day. → keep RabbitMQ, don't claim Kafka
4. **Go**
   No. → left out
5. **Distributed systems**
   The payment reconciliation flow runs across 3 services that talk through RabbitMQ; I built the retry and idempotency part so payments are never applied twice.
6. **On-call / production debugging**
   Yes, one week a month. I added alerts and a runbook; repeat alerts went down by about 40%.
7. **Testing (unit + integration)**
   JUnit and Testcontainers. I raised the payments module coverage from 45% to 78%.
8. **Redis / caching** (you list Redis but never say how)
   Cached merchant config in Redis; the config API went from ~120 ms to ~15 ms.
9. **Code reviews / design docs**
   I review PRs for 2 juniors and wrote the design doc for the reconciliation retry flow.
