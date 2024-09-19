from __future__ import unicode_literals
import json
import youtube_dl


ydl_opts = {}

def songDownload(fileDirectory):
    with open(fileDirectory+"/linksCollected.json", 'r') as json_file:
        data = json.load(json_file)

        
    links = data

    for link in links:

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])

            break
        break

songDownload()