from pytube import YouTube

def Download(link):  
    object = YouTube(link)
    object = object.streams.get_highest_resolution()
    try:
        object.download()
    except Exception:
        print("An error has occurred")
    print("Download is completed successfully")
link = input("Enter the YouTube videos URL:")
Download(link)
    