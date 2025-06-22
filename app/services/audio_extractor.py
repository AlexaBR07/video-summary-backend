from moviepy.editor import VideoFileClip
import os

def extract_audio(video_path: str, output_dir: str = "audios") -> str:
    os.makedirs(output_dir, exist_ok=True)
    base_name = os.path.splitext(os.path.basename(video_path))[0]
    audio_path = os.path.join(output_dir, f"{base_name}.wav")

    clip = VideoFileClip(video_path)
    clip.audio.write_audiofile(audio_path)

    return audio_path
