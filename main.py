from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import os
from app.audio_extractor import extract_audio

app = FastAPI()

# Permitir conexiones desde cualquier origen (útil para pruebas locales)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Crear carpeta temporal si no existe
os.makedirs("temp", exist_ok=True)

@app.post("/upload/")
async def upload_video(file: UploadFile = File(...)):
    video_path = f"temp/{file.filename}"
    with open(video_path, "wb") as f:
        f.write(await file.read())

    # 1. Extraer audio
    audio_path = extract_audio(video_path)

    return {
        "filename": file.filename,
        "audio_path": audio_path
    }
