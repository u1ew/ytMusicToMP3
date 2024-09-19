from __future__ import unicode_literals
import yt_dlp as youtube_dl



def download_music(path, url):
    ydl_opts = {
        'format': 'bestaudio/best',  # Download the best audio quality
        'outtmpl': path,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])