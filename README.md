# Backend - Procesador de Videos con Resumen Automático

Este es el backend del proyecto **"Procesador de Videos con Resumen Automático"**, desarrollado en Python con FastAPI. Permite recibir un archivo de video, extraer su audio, transcribir el contenido y generar un resumen textual mediante modelos de inteligencia artificial.

## Funcionalidades

- **Subida de videos** vía API con `FastAPI` y `UploadFile`
- **Extracción de audio** desde el video usando `moviepy==1.0.3` y `pydub`
- **Transcripción automática** del audio mediante `openai-whisper` (requiere `torch`)
- **Generación de resumen** utilizando el modelo `facebook/bart-large-cnn` con `transformers`
- **Respuesta estructurada** en formato JSON que incluye:
  - Transcripción completa del video
  - Resumen del contenido

## Requisitos

- Python 3.9 o superior
- ffmpeg (debe estar instalado en el sistema)

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

# Ejecución del Servidor
uvicorn app.main:app --reload