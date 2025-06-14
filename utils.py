import re

def check_youtube_link(link):
    """Check if entry is a Youtube Link"""
    regex_pattern = re.compile(r'^((?:https?:)?\/\/)?((?:www|m)\.)?((?:youtube\.com|youtu.be))(\/(?:[\w\-]+\?v=|embed\/|v\/)?)([\w\-]+)(\S+)?$', re.IGNORECASE)

    return bool(regex_pattern.match(link))

def yt_dlp_opts(path):
    """yt-dlp options"""
    ydl_opts = {
        'outtmpl': path
    }

    audio_only = input("Do you want it as audio only? [Y]es, [N]o\n\n")

    if audio_only == 'y':
        ydl_opts['postprocessors'] = [{'key': 'FFmpegExtractAudio'}]
    
    return ydl_opts
