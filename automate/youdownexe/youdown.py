import youtube_dl
import pyfiglet

title = pyfiglet.figlet_format("!!YOUDOWN!!")
print(title)
print("by DERTY")
print("<------------------------------------------------>")

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


downmp3()

