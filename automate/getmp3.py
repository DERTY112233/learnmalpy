import re
import os
import subprocess
import yt_dlp
import pyfiglet

title = pyfiglet.figlet_format("YouDown v3", "5lineoblique")

print(title)

URLS = str(input("YT Links: "))


ydl_opts = {
    'format': 'mp3/bestaudio/best',
    'postprocessors': [{  # Extract audio using ffmpeg
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
    }]
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    error_code = ydl.download(URLS)

content_name = re.compile("(Sermon Only)/(sermon only)/(Sermon only)")

dirs = os.scandir("~/Music/")
dirs = enumerate(dirs)