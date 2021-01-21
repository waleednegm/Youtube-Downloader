import downloader

def download():
    youtube_link = input("Enter The Link of youtube video ? ")
    print("1 - 144p")
    print("2 - 240p")
    print("3 - 360p")
    print("4 - 480p")
    print("5 - 720p")
    quality = input("choose [1-5]:  ")
    if(quality =="1"):
        downloader.download_video(youtube_link,"144p")
    elif (quality =="2"):
        downloader.download_video(youtube_link,"240p")
    elif (quality =="3"):
        downloader.download_video(youtube_link,"360p")
    elif (quality =="4"):
        downloader.download_video(youtube_link,"480p")
    elif (quality =="5"):
        downloader.download_video(youtube_link,"720p")
    else:
        print("Wrong Choice")