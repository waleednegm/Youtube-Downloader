import pytube

def download_video(video,quailty):
    try:
        video.streams.filter(res=quailty).first().download()
        print("video has been downloaded")
    except :
        print("This quailty not available for this video")