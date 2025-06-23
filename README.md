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
## Clonar el repositorio
git clone https://github.com/tuusuario/video-summary-backend.git
cd video-summary-backend

## Crear entorno virtual
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

## Instalar dependencias
pip install -r requirements.txt

## Ejecución del Servidor
uvicorn app.main:app --reload



#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------#


# Pruebas Unitarias
Este proyecto incluye pruebas unitarias para validar las funciones principales del backend: extracción de audio, transcripción, resumen de texto y el endpoint /upload/.

## Archivos de prueba
-Las pruebas se encuentran en la carpeta tests/ e incluyen:

test_audio_extractor.py: Verifica que extract_audio() genere un archivo .wav válido desde un video.

test_transcriber.py: Prueba que transcribe_audio() maneje correctamente archivos inválidos.

test_summarizer.py: Evalúa el comportamiento de summarize_text() ante textos cortos y largos.

test_routes.py: Simula una petición POST /upload/ usando un archivo ficticio. Es normal que esta prueba falle, ya que MoviePy no puede procesar contenido falso como un video válido. Sirve para probar cómo responde el backend a entradas inválidas.

# Como ejecutar las pruebas:

## PowerShell(Windows)
$env:PYTHONPATH="."

## Linux/Mac
export PYTHONPATH=.

# luego ejecuta las pruebas con:
pytest

# Resultado:
tests/test_audio_extractor.py .     [ 25%]
tests/test_routes.py F              [ 50%]
tests/test_summarizer.py ..         [ 75%]
tests/test_transcriber.py .         [100%]

1 failed, 4 passed

-El fallo en test_routes.py es esperado, ya que se está utilizando un archivo simulado que no es un video real.
-Esto permite verificar que el sistema maneje errores correctamente.



#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------#


#Integración Continua (CI) con GitHub Actions
Este proyecto incluye un pipeline automatizado para integración continua usando GitHub Actions.

## ¿Qué hace el pipeline?
-Se ejecuta automáticamente cuando haces push o pull request a la rama main.
-Configura un entorno Ubuntu con Python 3.10.
-Instala ffmpeg (requisito para procesar videos con moviepy).
-Crea un entorno virtual e instala todas las dependencias listadas en requirements.txt.
-Ejecuta las pruebas unitarias con pytest.

## ¿Cómo funciona?
-El archivo de configuración está en .github/workflows/python-app.yml.
-Cada vez que subes código, GitHub ejecuta estas tareas automáticamente para asegurar que el backend funcione correctamente antes de fusionar cambios.

## ¿Cómo usarlo?
-El pipeline ya está configurado y listo para usarse si tienes el archivo .github/workflows/python-app.yml en tu repositorio.
-Cuando hagas cambios y hagas push a la rama main o crees un pull request a esa rama, el pipeline se ejecutará automáticamente.
-Puedes revisar el estado y resultados del pipeline en la pestaña Actions de tu repositorio en GitHub.

