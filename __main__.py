import csv
import os
import re

def youtube_link(entry):
    """Check if csv entry is a Youtube Link"""
    link_pattern = re.compile(r'(?:https?:\/\/)?(?:www\.)?(?:youtu\.be\/|youtube\.com\/(?:embed\/|v\/|playlist\?|watch\?v=|watch\?.+(?:&|&#38;);v=))([a-zA-Z0-9\-_]{11})?(?:(?:\?|&|&#38;)index=((?:\d){1,3}))?(?:(?:\?|&|&#38;)?list=([a-zA-Z\-_0-9]{34}))?(?:\S+)?', re.IGNORECASE)

    return bool(link_pattern.match(entry))

def file_location():
    """Ask user for file location"""
    
    home_directory = os.path.expanduser('~')
    documents_directory = os.path.join(home_directory, 'Documents')

    while True:
        user_input = input("What is the CSV file's name?\n(Please keep the file in Documents otherwise the script cannot find it. Don't add file extension)\n")
        user_input += '.csv'
        file_path = os.path.join(documents_directory, user_input)
        print(file_path)

        if not os.path.exists(file_path):
            print(f'File {user_input} was not found in {documents_directory}.\nCheck name is in correct and file is in correct location and try again.')
            continue

        return file_path


def read_csv(file_path):
    """Reads csv file"""
    try:
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            entries = csv.reader(csvfile)
            for row in entries:
                for cell in row:
                    print(youtube_link(cell))
    except Exception as e:
        print(f'Error:\n{e}')
        # return []


def additional_args():
    """Ask user whether they want to add additional arguments (for now only ask save location)"""


if __name__ == "__main__":
    csv_location = file_location()
    read_csv(csv_location)
