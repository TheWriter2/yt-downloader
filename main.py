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
        
        self.videoDict = {
            "format":"mp4",
            #"format-sort":"+size,+br,+res,+fps",
            "ignoreerrors": True
        }

        self.audioDict = {
            "format":"mp3",
            "postprocessors": [{  # Extract audio using ffmpeg
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
            }],
            "ignoreerrors": True
        }

        # Video and audio
        self.Downloader = yt_dlp.YoutubeDL(self.videoDict)

        # Audio only
        self.Downloader_MP3 = yt_dlp.YoutubeDL(self.audioDict)

        # Flags
        self.downloadMP3 = False
        self.videoFormats = ["flv", "m4a", "mp4", "webm"]
        self.audioFormats = ["3gp", "aac", "mp3", "ogg", "wav"]
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
            choosing = choice.inputchoice(self.videoFormats, "Select a format:")

            self.videoDict["format"] = self.videoFormats[choosing - 1] + "/b*"
            self.Downloader = yt_dlp.YoutubeDL(self.videoDict)

            self.Downloader.cache.remove()
            self.Downloader.download([link])
        else:
            choosing = choice.inputchoice(self.audioFormats, "Select a format:")

            self.audioDict["format"] = self.audioFormats[choosing - 1] + "/b*"
            self.Downloader_MP3 = yt_dlp.YoutubeDL(self.audioDict)

            self.Downloader_MP3.cache.remove()
            self.Downloader_MP3.download([link])
        
        if link[24:32] == "playlist":
            os.chdir("..")
        
        self.mainmenu()

if __name__ == "__main__":
    cur_run = VideoDownloader()
    cur_run.mainmenu()