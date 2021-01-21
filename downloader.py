import pytube

def download_video(youtube_link,quailty):
    try:
        pytube.YouTube(youtube_link).streams.filter(res=quailty,progressive=True).first().download()
        print("The video has been downloaded")
    except :
        print("This quailty not available for this video")
