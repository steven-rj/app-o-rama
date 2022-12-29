import sys
import time
import os

import youtube_downloader as yt
import pdf_speech as pdf
import bigclipboard as clipb


def clear_screen():
    os.system('cls')

def display_main_menu():

    options = ["Big Clipboard", "PDF-to-Speech", "YouTube Downloader"]
    app_num = -1

    print("\n================")
    print("App-o-Rama v0.1")
    print("================\n")
    print("Exit Program: 0")
    for i, option in enumerate(options, 1):
        print(f"{i}: {option}")

    app_num = int(input("\nChoose option by number: "))

    if app_num == 0:
        sys.exit()
    elif app_num == 1:
        print("\nLoading Big Clipboard..\n")
        time.sleep(1)
        clear_screen()
        clipb.main()
    elif app_num == 2:
        print("\nLoading PDF-to-Speech..\n")
        time.sleep(1)
        clear_screen()
        pdf.main()
    elif app_num == 3:
        print("\nLoading YouTube Downloader..\n")
        time.sleep(1)
        clear_screen()
        yt.main()
    else:
        print("Please select a valid option")
        time.sleep(1)
        display_main_menu()

if __name__ == "__main__":
    display_main_menu()
