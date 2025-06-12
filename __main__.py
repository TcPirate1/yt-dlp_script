
import csv
import os
from yt_dlp import YoutubeDL
from utils import discover_os, check_youtube_link

def file_location():
    """Ask user for information related to YT-DLP"""
    
    home_directory = os.path.expanduser('~')

    while True:
        file_path_input = input("Where do you want to save the file?\n\n")
        file_path = f'{os.path.join(home_directory, file_path)}'
        
        confirmation = input(f'Are you sure you want to save in {file_path}? [Y]es, [N]o\n\n')

        if confirmation.lower() == 'y':
            return file_path
        else:
            print("Exiting...")
            continue

def audio_arguments():
    """Ask user for additional arguments"""
    arguments_input = input("Do you want specific audio format? [Y]es, [N]o\n\n")

    if arguments_input.lower == 'y':
        options = input("What is the format?\n")
        return options

def run_yt_dlp():
    """Runs the yt-dlp utility"""

    yt_link = input("Enter the link:\n")
    
    if check_youtube_link(yt_link) == False:
        print("It appears your link isn't a YT link. Please enter a valid link.")

    path = file_location()

    arguments = audio_arguments()

    
    ydl_opts = {
        'format': arguments,
        'outtmlp': path
    }
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download(yt_link)


if __name__ == "__main__":
    run_yt_dlp()
