from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.upload import router as upload_router
import os

app = FastAPI()

# Middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Asegurar que carpetas necesarias existan
os.makedirs("temp", exist_ok=True)
os.makedirs("audios", exist_ok=True)

# Incluir las rutas
app.include_router(upload_router, prefix="/upload", tags=["Upload"])
