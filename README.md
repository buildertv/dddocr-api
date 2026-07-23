# ddddocr API (FastAPI + Docker)

🇺🇸 English | **[🇻🇳 Tiếng Việt](README_vi.md)**

Simple REST API for CAPTCHA recognition using the **ddddocr** Python library.

## Features

* 🚀 FastAPI REST API
* 🔍 CAPTCHA recognition with ddddocr
* 🐳 Docker & Docker Compose support
* 📦 Lightweight deployment
* 🌐 Easy integration with other applications

## Project Structure

```text
.
├── app.py
├── Dockerfile
├── docker-compose.yml
└── requirements.txt
```

## Run with Docker

```bash
docker compose up -d --build
```

Open Swagger:

```
http://localhost:8002/docs
```

## Run without Docker

Install dependencies:

```bash
pip install -r requirements.txt
```

Run:

```bash
uvicorn app:app --host 0.0.0.0 --port 8000
```

## API

### OCR from URL

```
POST /ocr/url
```

Example:

```bash
curl -X POST "http://localhost:8002/ocr/url?url=https://example.com/captcha.png"
```

### OCR from File

```
POST /ocr/file
```

Example:

```bash
curl -X POST -F "file=@captcha.png" http://localhost:8002/ocr/file
```

## Docker Port

```yaml
ports:
  - "8002:8000"
```

The API will be available at:

```
http://YOUR_SERVER_IP:8002
```

## License

MIT
