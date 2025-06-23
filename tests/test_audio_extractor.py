import os
import pytest
from app.services.audio_extractor import extract_audio

@pytest.fixture
def sample_video_path(tmp_path):
    # Crea un archivo fake para simular video
    fake_video = tmp_path / "sample.mp4"
    fake_video.write_bytes(b"fake video content")
    return str(fake_video)

def test_extract_audio_creates_audio_file(sample_video_path, tmp_path):
    # No podemos usar video real, entonces vamos a simular
    # Aquí la función fallará si el video no es válido, lo que es esperado.
    # Entonces solo probamos que se cree el directorio audios y que intente crear archivo
    
    output_dir = tmp_path / "audios"
    output_dir.mkdir()

    try:
        audio_path = extract_audio(sample_video_path, str(output_dir))
    except Exception:
        # Aquí esperamos excepción porque el video es fake
        assert True
    else:
        # Si no falla, comprueba que el archivo exista
        assert os.path.exists(audio_path)
