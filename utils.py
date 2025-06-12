import platform
import re

def discover_os():
    """Gives program what OS is being ran"""
    return platform.system()

def check_youtube_link(link):
    """Check if csv entry is a Youtube Link"""
    regex_pattern = re.compile(r'^((?:https?:)?\/\/)?((?:www|m)\.)?((?:youtube\.com|youtu.be))(\/(?:[\w\-]+\?v=|embed\/|v\/)?)([\w\-]+)(\S+)?$', re.IGNORECASE)

    return bool(regex_pattern.match(link))