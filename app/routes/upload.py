from fastapi import APIRouter, UploadFile, File
import os
from app.services.audio_extractor import extract_audio
from app.services.transcriber import transcribe_audio
from app.services.summarizer import summarize_text

router = APIRouter()

@router.post("/")
async def upload_video(file: UploadFile = File(...)):
    video_path = f"temp/{file.filename}"
    with open(video_path, "wb") as f:
        f.write(await file.read())

    audio_path = extract_audio(video_path)
    transcription = transcribe_audio(audio_path)
    summary = summarize_text(transcription)

    return {
        "transcription": transcription,
        "summary": summary
    }