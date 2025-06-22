from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import os
from app.audio_extractor import extract_audio
from app.transcriber import transcribe_audio
from app.summarizer import summarize_text

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

    # 2. Transcribir audio
    transcription = transcribe_audio(audio_path)

    # 3. Resumir transcripción
    summary = summarize_text(transcription)

    print(f"Transcription for {file.filename} completed successfully.")
    return {
        "transcription": transcription,
        "summary": summary
    }