import sys
import time
import os

import youtube_downloader as yt


def clear_screen():
    os.system('cls')

def display_main_menu():

    options = ["PDF-to-Speech", "YouTube Downloader", "Exit"]
    app_num = 0

    print("\n================")
    print("App-o-Rama v0.1")
    print("================\n")

    for i, option in enumerate(options, 1):
        print(f"{i}: {option}")

    app_num = int(input("\nChoose option by number: "))

    if app_num == 1:
        print("\nLoading PDF-to-Speech..\n")
        time.sleep(1)
        #display_diagnostics_menu()
    elif app_num == 2:
        print("\nLoading YouTube Downloader..\n")
        time.sleep(1)
        clear_screen()
        yt.main()
    elif app_num == 3:
        sys.exit()
    else:
        print("Please select a valid option")
        time.sleep(1)
        display_main_menu()

if __name__ == "__main__":
    display_main_menu()
