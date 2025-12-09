# Contact Book API
A REST api to manage contact book. Built to learn Python, Flask, SQLAlchemy, Validation patterns and Exception handling.

## Tech Stack
- Flask
- Gunicorn
- SQLAlchemy
- Postgres
- Docker

## Running Locally
```bash
docker compose up --build
```

## Verify Application
```bash
curl http://localhost:5000/health
```

Expected output:
```json
{
  "status": "healthy"
}
```
## Teardown the app
```bash
docker compose down -v
```
