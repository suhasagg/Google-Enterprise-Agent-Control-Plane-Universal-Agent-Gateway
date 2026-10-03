# Distributed Runtime

SQL state + transactional outbox -> Kafka/Pulsar -> scheduler -> leased/fenced workers. Idempotency protects duplicate delivery; UNKNOWN/reconciliation handles ambiguous external effects.
