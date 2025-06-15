
import os
# from argparse import ArgumentParser
import csv
from yt_dlp import YoutubeDL
from yt_dlp.utils import read_batch_urls
from utils import check_youtube_link, yt_dlp_opts

# parser = ArgumentParser(prog="YT-DLP script")

def file_location():
    """Ask user for name of CSV file"""

    while True:
        file_name = input("What is the name of the CSV file? DO NOT add extension.\n\n")
        
        documents_directory = f'{os.path.join(os.path.expanduser('~'), "Documents", file_name)}.csv'

        if not os.path.exists(documents_directory):
            print(f'{file_name} was not found in {documents_directory}.\nCheck you did not make any typos and try again.')

        return documents_directory

def read_csv(documents):
    """Read the CSV file defined by the user"""
    with open(documents, newline='', encoding='utf-8') as csvfile:
        entries = csv.reader(csvfile)
        song_list = []
        for row in entries:
            for cell in row:
                if check_youtube_link(cell.strip()):
                    print(f'Add {cell} to separate txt file. Then run batch url function.')
                    song_list.append(cell)
    song_list_text = f'{os.path.expanduser('~')}/Documents/song_list.txt'
    with open(song_list_text, "w", encoding='utf-8') as songs:
        songs.write('\n'.join(str(i) for i in song_list))
    return song_list_text

def run_yt_dlp():
    """Runs the yt-dlp utility"""

    documents_path = file_location()
    print("Reading csv...")
    song_list_text_file = read_csv(documents=documents_path)

    read_batch_urls(song_list_text_file)

    # outtmpl = os.path.join(path,'%(title)s.%(ext)s')

    # with YoutubeDL(yt_dlp_opts(outtmpl)) as ydl:
    #     ydl.download(yt_link)


if __name__ == "__main__":
    run_yt_dlp()
