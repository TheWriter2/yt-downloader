import os
import sys
import choice
import yt_dlp

# Getting current directory
os.chdir(os.path.dirname(sys.argv[0]))

# Getting the folder to download the files into
try:
    os.chdir("./downloads/")
except:
    os.mkdir("downloads")
    os.chdir("./downloads/")

# Main class
class VideoDownloader:
    def __init__(self):
        
        # Video and audio
        self.Downloader = yt_dlp.YoutubeDL({
            "format":"mp4/bv*[height<=480]+ba/b[height<=480] / wv*+ba/w",
            "ignoreerrors": True
        })

        # Audio only
        self.Downloader_MP3 = yt_dlp.YoutubeDL({
            "format":"mp3/bestaudio/best",
            "postprocessors": [{  # Extract audio using ffmpeg
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
            }],
            "ignoreerrors": True
        })

        # Flags
        self.downloadMP3 = False
    def mainmenu(self):
        choosing = choice.inputchoice(["Download Video", "Download Video (audio only)", "Exit"], "Welcome! What do you want to do?")

        if choosing == 3:
            sys.exit()
        elif choosing == 1:
            self.downloadMP3 = False
            self.download()
        elif choosing == 2:
            self.downloadMP3 = True
            self.download()
    
    def download(self):
        link = input("Copy & paste the URL of the youtube video you want to download:\n")
        
        if link[24:32] == "playlist":
            self.Downloader.cache.remove()
            playlist_info = self.Downloader.extract_info(link, download=False)
            
            os.mkdir(playlist_info.get("title"))
            os.chdir("./{}/".format(playlist_info.get("title")))

        if self.downloadMP3 == False:
            self.Downloader.cache.remove()
            self.Downloader.download([link])
        else:
            self.Downloader_MP3.cache.remove()
            self.Downloader_MP3.download([link])
        
        if link[24:32] == "playlist":
            os.chdir("..")
        
        self.mainmenu()

if __name__ == "__main__":
    cur_run = VideoDownloader()
    cur_run.mainmenu()