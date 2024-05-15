from pytube import *
import tqdm
import os
import time


path = os.path.dirname(os.path.abspath(__file__))

if not os.path.isdir(path):
    os.mkdir(os.path.join(path, "Video Downloader"))


# add progression bar to this 
def videoDownload(link):
    try:
            yt = YouTube(link)
            print("Fazendo o download do video " + yt.title)
            for i in tqdm.tqdm(range(1)):
                video = yt.streams.filter(file_extension="mp4").get_highest_resolution()
                video.download(path + "/Video Downloader/Videos", yt.title + ".mp4")
            print("Download realizado com sucesso! Arquivo salvo em " + path + "/Video Downloader/Videos")
    except Exception as e:
        print(e)


def playlistDownload(link):
    try:
        p = Playlist(link)
        print("Fazendo o download dos videos em " + p.title)
        for video in tqdm.tqdm(p.videos):
            video = video.streams.filter(file_extension="mp4").get_highest_resolution()
            video.download(path + "/Video Downloader/Playlist", video.title + ".mp4")
        print("Download realizado com sucesso! Arquivos salvos em " + path + "/Video Downloader/Playlist")
    except Exception as e:
        print(e)