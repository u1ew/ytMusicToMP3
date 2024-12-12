import yt_dlp as youtube_dl

def download_playlist(url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'ignoreerrors': True,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

# Function that downloads playlist to mp3

arrSongs = []

while True:
    print("Input playlist or song link to be added to download list (to cancel input nothing):")
    sUserInput = str(input())

    if len(sUserInput) > 0:
        arrSongs.append(sUserInput)
    else:
        False
        for song in arrSongs:
            download_playlist(song)
        exit()