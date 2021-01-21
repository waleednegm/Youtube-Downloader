import video
import playlist


if __name__ == "__main__":
    print("1- download 1 video ")
    print("2- download playlist")
    choose = input("choose [1-2]:  ")
    if (choose=="1"):
        video.download()
    elif(choose =="2"):
        playlist.download()
    

    
