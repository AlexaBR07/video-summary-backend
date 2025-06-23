import pytest
from app.services.transcriber import transcribe_audio

def test_transcribe_audio_with_invalid_path():
    with pytest.raises(Exception):
        transcribe_audio("nonexistent_audio.wav")

#Nota: 
# Para pruebas reales se necesitaría un archivo .wav válido. 
# Para un test completo, tendrías que incluir un audio pequeño en el repositorio o mockear whisper.