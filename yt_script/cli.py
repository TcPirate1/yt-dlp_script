
import os
# from argparse import ArgumentParser
from yt_dlp import YoutubeDL
from yt_dlp.utils import read_batch_urls
from yt_script.utils import check_youtube_link, yt_dlp_opts
import csv

# parser = ArgumentParser(prog="YT-DLP script")

def file_location():
    """Ask user for name of CSV file"""

    while True:
        file_name = input("What is the name of the CSV file? DO NOT add extension.\n\n")
        
        documents_directory = os.path.join(os.path.expanduser('~'), "Documents", file_name, ".csv")

        if not os.path.exists(documents_directory):
            print(f'{file_name} was not found in {documents_directory}.\nCheck you did not make any typos and try again.')

        return documents_directory

def read_csv(documents):
    with open(documents, newline='', encoding='utf-8') as csv:
        entries = csv.reader(csvfile=csv)
        for row in entries:
            for cell in row:
                if check_youtube_link(cell.strip()):
                    print(f'Add {cell} to separate txt file. Then run batch url function.')

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


if __name__ == "__main__":
    run_yt_dlp()
