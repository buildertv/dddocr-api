# ddddocr API (FastAPI + Docker)

Simple REST API for CAPTCHA recognition using the **ddddocr** Python library.

## Features

* 🚀 FastAPI REST API
* 🔍 CAPTCHA recognition with `ddddocr`
* 🐳 Docker & Docker Compose support
* 📦 Lightweight deployment
* 🌐 HTTP API for easy integration

---

## Project Structure

```text
.
├── app.py
├── Dockerfile
├── docker-compose.yml
└── requirements.txt
```

---

## Requirements

* Docker
* Docker Compose

or

* Python 3.11+

---

## Run with Docker

Build and start the container:

```bash
docker compose up -d --build
```

View logs:

```bash
docker logs -f ddddocr
```

Stop the container:

```bash
docker compose down
```

The API will be available at:

```
http://localhost:8002
```

Swagger UI:

```
http://localhost:8002/docs
```

ReDoc:

```
http://localhost:8002/redoc
```

---

## Run without Docker

Install dependencies:

```bash
pip install -r requirements.txt
```

Start the API:

```bash
uvicorn app:app --host 0.0.0.0 --port 8000
```

Open:

```
http://localhost:8000/docs
```

---

## API Usage

### Recognize CAPTCHA from Image URL

**POST**

```
/ocr/url
```

Example:

```bash
curl -X POST \
"http://localhost:8002/ocr/url?url=https://example.com/captcha.png"
```

Example Response

```json
{
  "success": true,
  "text": "8A6K"
}
```

---

### Recognize CAPTCHA from Uploaded Image

**POST**

```
/ocr/file
```

Example:

```bash
curl -X POST \
  -F "file=@captcha.png" \
  http://localhost:8002/ocr/file
```

Example Response

```json
{
  "success": true,
  "text": "X9PD"
}
```

---

## Docker Configuration

The container exposes port **8000**, mapped to host port **8002**.

```yaml
ports:
  - "8002:8000"
```

So the API can be accessed via:

```
http://YOUR_SERVER_IP:8002
```

---

## Dockerfile

The image uses:

* Python 3.11 Slim
* FastAPI
* Uvicorn
* ddddocr

Startup command:

```bash
uvicorn app:app --host 0.0.0.0 --port 8000
```

---

## License

MIT
