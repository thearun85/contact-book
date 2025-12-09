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

## Verify Database
```bash
docker compose exec db psql -U contactbook -d contactbook -c '\dt'
```
Expected Output:
```
            List of relations
 Schema |   Name   | Type  |    Owner
--------+----------+-------+-------------
 public | contacts | table | contactbook
 public | emails   | table | contactbook
 public | phones   | table | contactbook
(3 rows)
```

## API Endpoints
| Path | Method | Description |
|------|--------|-------------|
| /api/v1/contacts | POST | Create contact |
| /api/v1/contacts | GET | List all contacts |

## Example Requests

**Create:**
```bash
curl -X POST http://localhost:5000/api/v1/contacts \
  -H "Content-Type: application/json" \
  -d '{
    "first_name": "Jane",
    "last_name": "Doe",
    "emails": [{"email": "jane@example.com", "label": "work", "is_primary": true}],
    "phones": [{"number": "+14155551234", "label": "mobile", "is_primary": true}]
  }'
```

**List all:**
```bash
curl http://localhost:5000/api/v1/contacts
```

## Teardown the app
```bash
docker compose down -v
```
