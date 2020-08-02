try:
    from pytube import YouTube
    from pytube import Playlist
    from moviepy.editor import *
    import os
    import re
    import shutil
except Exception as exc:
    print('Missing modules:', exc)

invalid_characters = ['<', '>', ':', '"', '/', '\\', '|', '?', '*', '.', ',', "'", '$']


def download_video(url, location):
    video = YouTube(url)

    for stream in video.streams:
        if stream.mime_type == 'audio/mp4':
            title = ''

            for char in list(video.title):
                if char not in invalid_characters:
                    title += char
            stream.download()
            
            clip = AudioFileClip(os.path.join(os.getcwd(), '{}.mp4'.format(title)))
            clip.write_audiofile(os.path.join(os.getcwd(), '{}.mp3'.format(title)))
            clip.close()

            os.remove(os.path.join(os.getcwd(), '{}.mp4'.format(title)))
            shutil.move(os.path.join(os.getcwd(), '{}.mp3'.format(title)), os.path.join(location, '{}.mp3'.format(title)))
            break


def download_playlist(url, location):
    playlist = Playlist(url)

    playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")
    for url in playlist.video_urls:
        download_video(url, location)