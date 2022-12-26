from pytube import YouTube

import main_menu

def download(url):
    
    yt_object = YouTube(url)
    yt_object = yt_object.streams.get_highest_resolution()

    try:
        yt_object.download()
    except:
        print(f"Error downloading {url}!")
    
    print(f"{yt_object.title} downloaded successfully!")

def main():

    print("YouTube Downloader v1.0")
    url = input("Enter YouTube url to download: ")
    download(url)
    main_menu.display_main_menu()

if __name__ == "__main__":
    main()