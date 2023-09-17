import os
import sys
import choice
import yt_dlp

os.chdir(os.path.dirname(sys.argv[0]))

try:
    os.chdir("./downloads/")
except:
    os.mkdir("downloads")
    os.chdir("./downloads/")

class VideoDownloader:
    def __init__(self):
        self.Downloader = yt_dlp.YoutubeDL({
            "format":"mp4/bv*[height<=480]+ba/b[height<=480] / wv*+ba/w",
            "ignoreerrors": True
        })
        self.Downloader_MP3 = yt_dlp.YoutubeDL({
            "format":"mp3/bestaudio/best",
            "postprocessors": [{  # Extract audio using ffmpeg
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
            }],
            "ignoreerrors": True
        })
    def mainmenu(self):
        choosing = choice.inputchoice(["Download Video", "Download Video (audio only)", "Exit"], "Welcome! What do you want to do?")

        if choosing == 3:
            sys.exit()
        elif choosing == 1:
            self.download()
        elif choosing == 2:
            self.download_mp3()
    
    def download(self):
        link = input("Copy & paste the URL of the youtube video you want to download:\n")
        
        if link[24:32] == "playlist":
            self.Downloader.cache.remove()
            playlist_info = self.Downloader.extract_info(link, download=False)
            
            os.mkdir(playlist_info.get("title"))
            os.chdir("./{}/".format(playlist_info.get("title")))

            self.Downloader.download([link])
            os.chdir("../")
        else:
            self.Downloader.cache.remove()
            self.Downloader.download([link])
    
    def download_mp3(self):
        link = input("Copy & paste the URL of the youtube video you want to download:\n")

        if link[24:32] == "playlist":
            self.Downloader_MP3.cache.remove()
            playlist_info = self.Downloader_MP3.extract_info(link, download=False)

            print(playlist_info.get("title"))

            os.mkdir(playlist_info.get("title") + "_MP3")
            os.chdir("./{}/".format(playlist_info.get("title") + "_MP3"))

            print(os.getcwd())

            self.Downloader_MP3.download([link])
            os.chdir("../")
        else:
            self.Downloader_MP3.cache.remove()
            self.Downloader_MP3.download([link])

if __name__ == "__main__":
    cur_run = VideoDownloader()
    cur_run.mainmenu()