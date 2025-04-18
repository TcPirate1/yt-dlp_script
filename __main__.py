import platform
import csv
import os
import re
from yt_dlp import YoutubeDL

def discover_os():
    """Gives program what OS is being ran"""
    return platform.system()

def youtube_link(entry):
    """Check if csv entry is a Youtube Link"""
    link_pattern = re.compile(r'^((?:https?:)?\/\/)?((?:www|m)\.)?((?:youtube\.com|youtu.be))(\/(?:[\w\-]+\?v=|embed\/|v\/)?)([\w\-]+)(\S+)?$', re.IGNORECASE)

    return bool(link_pattern.match(entry))

def file_location():
    """Ask user for file location"""
    
    home_directory = os.path.expanduser('~')
    documents_directory = os.path.join(home_directory, 'Documents')

    while True:
        user_input = input("What is the CSV file's name?\n(Please keep the file in Documents otherwise the script cannot find it. Don't add file extension)\n")
        user_input += '.csv'
        file_path = os.path.join(documents_directory, user_input)

        if not os.path.exists(file_path):
            print(f'File {user_input} was not found in {documents_directory}.\nCheck name is in correct and file is in correct location and try again.')
            continue

        return file_path


def read_csv(file_path):
    """Reads csv file"""
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        entries = csv.reader(csvfile)
        for row in entries:
            for cell in row:
                if youtube_link(cell.strip()):
                    run_yt_dlp(cell.strip())

def run_yt_dlp(yt_link):
    """Runs the yt-dlp utility"""

    if discover_os() == 'Linux':
        path = f'{os.path.expanduser('~')}/Videos/Music'
    else:
        path = f'{os.path.expanduser('~')}/Music'
    
    ydl_opts = {
        'format': 'aac',
        'outtmlp': path
    }
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download(yt_link)


if __name__ == "__main__":
    csv_location = file_location()
    read_csv(csv_location)
