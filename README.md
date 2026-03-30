# Challenge API (FastAPI + Docker)

This project exposes a FastAPI endpoint that uploads a file to VirusTotal and returns the scan report.

## Prerequisites

- Docker Desktop (or Docker Engine) with `docker compose`
- A VirusTotal API key

## Configuration

Create a `.env` file in the project root:

```bash
VIRUS_TOTAL_API_KEY=your_key_here
```

Note: `.env` is ignored by git (see `.gitignore`).

## Run with Docker

Build and start the API:

```bash
docker compose up --build
```

The API will be available at:

- `http://localhost:8000`
- Swagger UI: `http://localhost:8000/docs`

## Test the endpoint

Upload a file for scanning:

```bash
curl -sS -X POST "http://localhost:8000/file/scan/" \
  -F "file=@./path/to/file"
```

## Stop

```bash
docker compose down
```

## Troubleshooting

- If requests fail with an auth error, confirm `VIRUS_TOTAL_API_KEY` is set in `.env`.
- If port `8000` is in use, stop the other process or change the port mapping in `docker-compose.yml`.
