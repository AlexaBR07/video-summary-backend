from moviepy.editor import VideoFileClip
import os

def extract_audio(video_path: str, output_dir: str = "audios") -> str:
    os.makedirs(output_dir, exist_ok=True)  # Crea la carpeta audios/ si no existe

    # Obtener nombre base del archivo sin extensión
    base_name = os.path.splitext(os.path.basename(video_path))[0]
    audio_path = os.path.join(output_dir, f"{base_name}.wav")

    clip = VideoFileClip(video_path)
    clip.audio.write_audiofile(audio_path)

    return audio_path

# Solo se ejecuta si se corre este archivo directamente
if __name__ == "__main__":
    input_dir = "videos"
    filename = "Funcion_Booleana_Protoboard.mp4"
    video_file = os.path.join(input_dir, filename)

    if not os.path.exists(video_file):
        print("El archivo no existe:", video_file)
    else:
        print("Extrayendo audio de:", video_file)
        audio_path = extract_audio(video_file)
        print("Audio guardado en:", audio_path)
