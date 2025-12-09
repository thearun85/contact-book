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

## Teardown the app
```bash
docker compose down -v
```
