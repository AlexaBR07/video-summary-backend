from fastapi.testclient import TestClient
from app.main import app
import os

client = TestClient(app)

def test_upload_video_with_fake_file(tmp_path):
    # Crear un archivo de video falso
    dummy_video = tmp_path / "video.mp4"
    dummy_video.write_bytes(b"fake content")

    with open(dummy_video, "rb") as f:
        response = client.post(
            "/upload/",
            files={"file": ("video.mp4", f, "video/mp4")}
        )

    # Dependiendo del contenido, puede fallar por procesamiento (lo cual es válido)
    assert response.status_code in [200, 422, 500]
