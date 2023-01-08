import main_menu

from pytube import YouTube


def download(url):
    
    yt_object = YouTube(url)
    yt_object = yt_object.streams.get_highest_resolution()

    try:
        yt_object.download()
    except:
        print(f"Error downloading {url}!")
    
    print(f"{yt_object.title} downloaded successfully!")


def main():
    """
    DOCSTRING: asks user for a YouTube URL as string,
    creates a YouTube object from it with its highest resolution,
    prints validation message if successful.
    """
    print("YouTube Downloader v1.0")
    url = input("Enter YouTube url to download: ")
    download(url)
    main_menu.display_main_menu()

if __name__ == "__main__":
    main()