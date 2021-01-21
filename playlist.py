import playlist_downloader
from pytube import Playlist

def download():
    youtube_link = input("Enter The Link of youtube playlist ? ")
    print("1 - 360p")
    print("2 - 720p")
    quality = input("choose [1-5]:  ")
    from pytube import Playlist
    pl = Playlist(youtube_link)
    for video in pl.videos:
        if (quality =="1"):
            playlist_downloader.download_video(video,"360p")
        elif (quality =="2"):
            playlist_downloader.download_video(video,"720p")
        else:
            print("Error")
