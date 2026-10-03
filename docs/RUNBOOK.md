# Runbook

```bash
cp .env.example .env
docker compose up --build -d
curl http://localhost:8000/health
curl http://localhost:8000/v1/registry -H 'x-api-key: change-me'
pytest -q
```
