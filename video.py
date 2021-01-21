import downloader

def download():
    youtube_link = input("Enter The Link of youtube video ? ")
    print("1 - 360p")
    print("2 - 720p")
    quality = input("choose [1-2]:  ")
    if (quality =="1"):
        downloader.download_video(youtube_link,"360p")
    elif (quality =="2"):
        downloader.download_video(youtube_link,"720p")
    else:
        print("Wrong Choice")
