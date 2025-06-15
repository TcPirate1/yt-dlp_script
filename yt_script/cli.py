
import os
from argparse import ArgumentParser
from yt_dlp import YoutubeDL
from yt_script.utils import check_youtube_link, yt_dlp_opts

parser = ArgumentParser(prog="YT-DLP script")

def file_location():
    """Ask user for information related to YT-DLP"""
    
    home_directory = os.path.expanduser('~')

    while True:
        file_path_input = input("Where do you want to save the file?\n\n")
        file_path = f'{os.path.join(home_directory, file_path_input)}'
        
        confirmation = input(f'Are you sure you want to save in {file_path}? [Y]es, [N]o\n\n')

        if confirmation.lower() == 'y' and confirmation.lower() == 'n' and os.path.isdir(file_path) is True:
            return file_path
        
        print("\nRe-enter file path, it is either invalid or you pressed [N]o:")


def run_yt_dlp():
    """Runs the yt-dlp utility"""

    while True:
        yt_link = input("Enter the link:\n")
        
        if check_youtube_link(yt_link) is False:
            print("It appears your link isn't a YT link. Please enter a valid link.")
            continue
        break

    path = file_location()

    outtmpl = os.path.join(path,'%(title)s.%(ext)s')

    with YoutubeDL(yt_dlp_opts(outtmpl)) as ydl:
        ydl.download(yt_link)

    print("Would you like to download another song? [Y]es [N]o\n")


if __name__ == "__main__":
    run_yt_dlp()
