# ddddocr API (FastAPI + Docker)

**[🇺🇸 English](README.md)** | 🇻🇳 Tiếng Việt

API nhận diện CAPTCHA sử dụng thư viện **ddddocr** viết bằng **Python + FastAPI**, hỗ trợ triển khai nhanh bằng Docker.

## Tính năng

* 🚀 Xây dựng bằng FastAPI
* 🔍 Nhận diện CAPTCHA với thư viện ddddocr
* 🐳 Hỗ trợ Docker và Docker Compose
* 📦 Triển khai nhanh trên VPS
* 🌐 Dễ dàng tích hợp vào các ứng dụng khác

## Cấu trúc dự án

```text
.
├── app.py
├── Dockerfile
├── docker-compose.yml
└── requirements.txt
```

## Chạy bằng Docker

Build và chạy:

```bash
docker compose up -d --build
```

Xem log:

```bash
docker logs -f ddddocr
```

Dừng container:

```bash
docker compose down
```

Swagger UI:

```
http://localhost:8002/docs
```

## Chạy trực tiếp bằng Python

Cài thư viện:

```bash
pip install -r requirements.txt
```

Khởi động API:

```bash
uvicorn app:app --host 0.0.0.0 --port 8000
```

## API

### Đọc CAPTCHA từ URL

```
POST /ocr/url
```

Ví dụ:

```bash
curl -X POST "http://localhost:8002/ocr/url?url=https://example.com/captcha.png"
```

### Đọc CAPTCHA từ File

```
POST /ocr/file
```

Ví dụ:

```bash
curl -X POST -F "file=@captcha.png" http://localhost:8002/ocr/file
```

## Cấu hình Docker

```yaml
ports:
  - "8002:8000"
```

Sau khi chạy, API sẽ truy cập tại:

```
http://YOUR_SERVER_IP:8002
```

## Giấy phép

MIT
