import yt_dlp
import os

saveLocation = ""

downAudioOnly = False
downVideoFormat = {
    "cookies-from-browser":"chrome",
    "format":"bv*[ext=mp4]+ba",
    "format-sort":"",
    "outtmpl":"%(title)s.%(ext)s"
}
downAudioFormat = {
    "cookies-from-browser":"chrome",
    "format":"ba[ext=mp3]",
    "format-sort":"",
    "outtmpl":"%(title)s.%(ext)s"
}

def setSaveLocation(newSaveLocation):
    if not os.path.isdir(newSaveLocation):
        return "1: Not a directory"
    
    saveLocation = newSaveLocation
    return "0"

def download(format, url):
    with yt_dlp.YoutubeDL(format) as ydl:
        ydl.download([url])