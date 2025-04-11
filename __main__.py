import platform
import csv
import os
import subprocess


def discover_os():
    """Gets the OS name of the machine script is ran from"""
    print(platform.system())


def file_location():
    """Ask user for file location"""
    user_input = input("Where is the CSV file? ( Start from \"home/{username}\" or \"C:\\Users\\{username}\" )\n")
    home_directory = os.path.expanduser('~')

    try:
        if (discover_os() == "Linux"):
            if (os.path.exists(f'{home_directory}/{user_input}')):
                subprocess.run([f'cd {home_directory}/{user_input}'])
        else:
            if (os.path.exists(f'{home_directory}\\{user_input}')):
                subprocess.run([f'cd {home_directory}\\{user_input}'])
    except:
        print("Pathing error")



def read_csv():
    """Reads csv file"""
    file_location()


def additional_args():
    """Ask user whether they want to add additional arguments (for now only ask save location)"""


if __name__ == "__main__":
    read_csv()
