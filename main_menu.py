import sys
import time
import os

import organize_apps as apps
import youtube_downloader as yt
import pdf_speech as pdf
import bigclipboard as clipb


def clear_screen():
    os.system('cls')


def wait_timer():
    time.sleep(1)


def display_main_menu():

    options = apps.organize_apps()
    choice = -1

    print()
    print("=" * 15)
    print("App-o-Rama v0.2")
    print("=" * 15, "\n")

    for option in options:
        app_num = option[0]
        app_name = option[1][0]
        print(f"{app_num}: {app_name}")

    print()

    choice = int(input("Enter number for selection: "))    
    program_file = options[choice][1][1]
    program_name = options[choice][1][0]

    print(f"\nLoading {program_name}..")
    wait_timer()
    clear_screen()
    exec(program_file)


if __name__ == "__main__":
    display_main_menu()
