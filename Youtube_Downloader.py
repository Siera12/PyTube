from pytube import YouTube

youtube_url = input("Enter link:  ")
yt_ob = YouTube(youtube_url)

print("Title: " + yt_ob.title + "\n")
print("Duration: "+ str((yt_ob.length/60)) +"min")

choice=int(input(">>>>>>>>>>>>>>Pick<<<<<<<<<<<<:\n 1.Video\n 2.Audio"))
if choice == 1:
    yt_ob.streams.last().download("C:/Users/Covid Potato/Desktop/py/video/")
elif choice == 2:
    yt_ob.streams.first().download("C:/Users/Covid Potato/Desktop/py/audio/")
        
print("---------------------------Download Succesfull----------------------------")
