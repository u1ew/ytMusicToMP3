import json
from pytube import YouTube
import os

def songDownload():
    with open(r'C:\Users\ewanj\Documents\CODING\ytMusicPlaylistDownload\linksCollected.json', 'r') as json_file:
        data = json.load(json_file)

        
    links = data

    for link in links:
        yt = YouTube(link)

        # Extract only audio
        audio_stream = yt.streams.filter(only_audio=True).first()

        # Download the audio file
        output_file = audio_stream.download()

        # Convert the file to MP3
        base, ext = os.path.splitext(output_file)   
        new_file = base + '.mp3'
        os.rename(output_file, new_file)

        print(f"{yt.title} has been successfully downloaded as an MP3.")

songDownload()