# Production Upgrade

OIDC/workload identity -> persistent transitions -> Alembic -> outbox publisher -> Kafka/Pulsar -> scheduler/workers -> leases/fencing/idempotency -> approval resume -> production MCP/A2A -> governed memory/artifacts -> OTel -> Kubernetes -> DR/security validation.
