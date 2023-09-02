import youtube_dl
import pyfiglet
import subprocess
import os

folder = "youdownmp3"

subprocess.call("clear", shell=True)
subprocess.call(f"mkdir '~/{folder}'")

title = pyfiglet.figlet_format("!!YOUDOWN!!")
print(f"{title}\nBY DERTY")
print("<------------------------------------------------>")
print(f"CREATED FOLDER {folder} WHERE MP3S WILL BE STORED IN")

resp = input("will you be downloading multiple mp3s? (yes or no): ")

def downmp3():
    vidurl = input("poot da YouTube video yoo-arr-el: ")
    vidinfo = youtube_dl.YoutubeDL().extract_info(url = vidurl, download = False)
    filename = f"{vidinfo['title']}.mp3"
    options = {'format':'bestaudio/best',
               'keepvideo':False,
               'outtmpl':filename}
    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([vidinfo['webpage_url']])
    print("Da download complete now... {}".format(filename))
    subprocess.call("mv {filename} {folder}")


def manymp3():
    if resp == "yes":
        downmp3()
        resp2 = input("continue? (yes or no): ")
        if resp2 == "yes":
            print("great more yoo-arr-els\n continuing...")
            downmp3()


manymp3()
