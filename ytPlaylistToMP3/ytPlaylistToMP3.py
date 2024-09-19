import yt_dlp as youtube_dl

def download_playlist(url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': 'C:\Users\ewanj\Documents\Dev\ytMusicToMP3\ytPlaylistToMP3\Songs',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

# Example usage
download_playlist('https://music.youtube.com/playlist?list=PLCK20UqkVhH5eoEcb5XvA1sSezmTPc2-Y&si=fD-4oxcPJUrW7hYE')