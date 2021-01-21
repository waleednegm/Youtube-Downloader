import playlist_downloader
from pytube import Playlist

def download():
    youtube_link = input("Enter The Link of youtube playlist ? ")
    print("1 - 144p")
    print("2 - 240p")
    print("3 - 360p")
    print("4 - 480p")
    print("5 - 720p")
    quality = input("choose [1-5]:  ")
    from pytube import Playlist
    pl = Playlist(youtube_link)
    for video in pl.videos:
        if(quality =="1"):
            playlist_downloader.download_video(video,"144p")
        elif (quality =="2"):
            playlist_downloader.download_video(video,"240p")
        elif (quality =="3"):
            playlist_downloader.download_video(video,"360p")
        elif (quality =="4"):
            playlist_downloader.download_video(video,"480p")
        elif (quality =="5"):
            playlist_downloader.download_video(video,"720p")
        else:
            print("Error")