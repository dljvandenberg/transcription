from pytube import YouTube
import whisper


def download_audio(url: str, output_dir: str) -> str:
    """
    Download a video from youtube and save it to the output path
    
    Args:
        url (str): The url of the video to download
        output_path (str): The path to save the video to
    Returns:
        str: The name of the downloaded file
    """
    yt = YouTube(url)
    audio_channel = yt.streams.filter(only_audio=True).first()
    filename = audio_channel.default_filename
    audio_channel.download(output_path=output_dir)
    return filename

def transcribe_audio(audio_path: str) -> str:
    """
    Transcribe an audio file using Whisper
    
    Args:
        audio_path (str): The path to the audio file to transcribe
    
    Returns:
        str: The transcribed text
    """
    model = whisper.load_model("base")
    transcription = model.transcribe(audio_path)
    return transcription['text']

def save_to_file(text: str, output_path: str) -> None:
    """
    Save text to a file
    
    Args:
        text (str): The text to save
        output_path (str): The path to save the text to
    """
    with open(output_path, "w") as f:
        f.write(text)
