# Backend - Procesador de Videos con Resumen Automático

Este es el backend del proyecto **"Procesador de Videos con Resumen Automático"**, desarrollado en Python con FastAPI. Permite recibir un archivo de video, extraer su audio, transcribir el contenido y generar un resumen textual mediante modelos de inteligencia artificial.

## Funcionalidades

- Subida de video vía API
- Extracción de audio con `moviepy==1.0.3`
- Transcripción automática con `Whisper`
- Generación de resumen con `transformers` (modelo BART o similar)
- Respuesta en formato JSON con transcripción y resumen

## Requisitos

- Python 3.9 o superior
- ffmpeg (instalado en el sistema)

## Instalación

```bash
# Clonar el repositorio
git clone https://github.com/tuusuario/video-summary-backend.git
cd video-summary-backend

# Crear entorno virtual
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt
