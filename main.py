
import os
from yt_dlp import YoutubeDL
from yt_dlp.utils import DownloadError
from utils import check_youtube_link

def file_location():
    """Ask user for information related to YT-DLP"""
    
    home_directory = os.path.expanduser('~')

    while True:
        file_path_input = input("Where do you want to save the file?\n\n")
        file_path = f'{os.path.join(home_directory, file_path_input)}'
        
        confirmation = input(f'Are you sure you want to save in {file_path}? [Y]es, [N]o\n\n')

        if confirmation.lower() == 'y' and os.path.isdir(file_path) is True:
            return file_path
        else:
            print("Invalid file path. Retry please.")


def run_yt_dlp():
    """Runs the yt-dlp utility"""

    yt_link = input("Enter the link:\n")
    
    # Change to while loop at later stage
    if check_youtube_link(yt_link) is False:
        print("It appears your link isn't a YT link. Please enter a valid link.")

    path = file_location()

    # audio_only = input("Do you want it as audio only? [Y]es, [N]o\n\n")

    
    ydl_opts = {
        'postprocessors': [{
            'key': 'FFmpegExtractAudio'
        }],
        'outtmpl': os.path.join(path,'%(title)s.%(ext)s'),
    }
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download(yt_link)


if __name__ == "__main__":
    run_yt_dlp()
