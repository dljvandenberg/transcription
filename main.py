# This script downloads audio from youtube and transcribes it using Whisper

from utils import download_audio, transcribe_audio, save_to_file

if __name__ == "__main__":
    AUDIO_DIR = "output/audio"
    TRANSCRIPTION_DIR = "output/transcription"

    url = input("Enter the url of the video to download: ")
    filename = download_audio(url, AUDIO_DIR)
    audio_path = f"{AUDIO_DIR}/{filename}"
    print(f"Audio channel downloaded to {audio_path}")

    transcription_path = f"{TRANSCRIPTION_DIR}/{filename}.txt"
    transcription = transcribe_audio(audio_path)
    save_to_file(transcription, transcription_path)
    print(f"Transcription saved to {transcription_path}")
