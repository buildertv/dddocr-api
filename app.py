import io
from fastapi import FastAPI, File, Header, HTTPException, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from PIL import Image
import requests
import ddddocr

API_KEY = "hoangtuan.net"

app = FastAPI()

# Bổ sung CORS để tránh lỗi "Failed to fetch" khi test trên Web/Swagger
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

ocr = ddddocr.DdddOcr(show_ad=False)


def check_key(key: str):
    if key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")


def process_image_bytes(raw_bytes: bytes) -> str:
    """Xử lý nền trong suốt (PNG) thành nền trắng chuẩn trước khi OCR"""
    try:
        img = Image.open(io.BytesIO(raw_bytes))

        # Nếu ảnh có kênh Alpha (RGBA), tạo nền trắng đè lên để tránh bị đen nền
        if img.mode in ("RGBA", "P", "LA"):
            background = Image.new("RGB", img.size, (255, 255, 255))
            if img.mode == "RGBA":
                background.paste(img, mask=img.split()[3])
            else:
                background.paste(img)
            img = background
        elif img.mode != "RGB":
            img = img.convert("RGB")

        # Chuyển lại thành bytes định dạng PNG chuẩn cho ddddocr
        buf = io.BytesIO()
        img.save(buf, format="PNG")
        clean_bytes = buf.getvalue()

        return ocr.classification(clean_bytes)
    except Exception as e:
        print(f"Lỗi xử lý ảnh: {e}")
        return ""


@app.post("/ocr/url")
async def ocr_url(url: str, x_api_key: str = Header(...)):
    check_key(x_api_key)
    try:
        response = requests.get(url, timeout=10)
        result = process_image_bytes(response.content)
        return {"success": True, "text": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.post("/ocr/file")
async def ocr_file(file: UploadFile = File(...), x_api_key: str = Header(...)):
    check_key(x_api_key)
    raw_bytes = await file.read()
    result = process_image_bytes(raw_bytes)
    return {"success": True, "text": result}
