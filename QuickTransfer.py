#!/usr/bin/env python3
import signal
import sys
from pytube import YouTube
from pytube import Playlist
import os
import sys
import subprocess
import click
import wget
import os.path
import re

quicktransfer = """
\033[91m\033[01m _____       _      _    _                        __
|  _  |     (_)    | |  | |                      / _|
| | | |_   _ _  ___| | _| |_ _ __ __ _ _ __  ___| |_ ___ _ __
| | | | | | | |/ __| |/ / __| '__/ _` | '_ \/ __|  _/ _ \ '__|
\ \/' / |_| | | (__|   <| |_| | | (_| | | | \__ \ ||  __/ |
 \_/\_\\__,_|_|\___|_|\_\\__|_|  \__,_|_| |_|___/_| \___|_|

                         \033[33mBy iBlaze
"""

myip = subprocess.getoutput("hostname -I | awk '{print $1}'")

def playlist(stream, chunk, bytes_remaining):
    count = subprocess.getoutput('find -mindepth 1 -type f -name "*.mp*" -printf x | wc -c')
    os.system("clear")
    print("" + quicktransfer)
    print('\033[92mDownloading \033[37m: \033[93m' + my_playlist.title)
    print('\033[92mPlaylist Length \033[37m: \033[93m{} Minutes - ( {} )'.format(round(length),length))
    print('\033[92mAll Videos \033[37m:\033[93m %s ' % len(my_playlist.video_urls))
    print('\033[92mDownloaded \033[37m:\033[93m ' + count)
    curr = stream.filesize - bytes_remaining
    done = int(50 * curr / stream.filesize)
    print("")
    sys.stdout.write("\r\033[37m[ {}{}\033[37m ] ".format('\033[32m=' * done, ' ' * (50-done)) )
    sys.stdout.flush()
    print("\033[93m" + video.title)

def vids(stream, chunk, bytes_remaining):
    os.system("clear")
    print("" + quicktransfer)
    print("\033[92mDownloading\033[37m :\033[93m " + my_video.title)
    print('\033[92mPlaylist Length \033[37m: \033[93m{} Minutes - ( {} )'.format(round(length),length))
    curr = stream.filesize - bytes_remaining
    done = int(50 * curr / stream.filesize)
    print("")
    sys.stdout.write("\r\033[37m[ {}{}\033[37m ] ".format('\033[32m=' * done, ' ' * (50-done)) )
    sys.stdout.flush()
    print("\033[93m" + my_video.title)

def wget_bar(current, total, width=100):
    os.system("clear")
    print("" + quicktransfer)
    print("")
    print("\033[92mDownloading \033[37m: \033[93m" + basename)
    print("")
    print('\033[94m%d%% \033[37m[\033[94m%d \033[37m/ \033[94m%d\033[37m] ' % (current / total * 100, current, total))

def signal_handler(sig, frame):
    print("\033[0m")
    print("")
    print("Goodbye...")
    print("")
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

os.system("clear")
print(quicktransfer + '''
\033[37m[ \033[31m1 \033[37m]  Youtube Playlist
\033[37m[ \033[31m2 \033[37m]  Youtube Video            \033[92mWhat Do You Want To Download?
\033[37m[ \033[31m3 \033[37m]  Other File
\033[37m[ \033[31mx \033[37m]  Exit
''')
question = input("\033[92mSelect \033[37m:\033[93m ")

if question == "1":
    print("")
    ply = input("\033[92mEnter Youtube Playlist Url \033[37m: \033[93m")
    my_playlist = Playlist(ply)
    lst = []
    print("")
    print("Calculating Playlist Length...")
    for video in my_playlist.videos:
        numbers = int(video.length)
        lst.append(numbers)
    length = (sum(lst)/60)
    print('\033[92mPlaylist Length \033[37m: \033[93m{} Minutes - ( {} )'.format(round(length),length))
    inp = ""
    while inp != "mp4" and inp != "mp3":
        print("")
        inp = input("\033[92mDownload Mp4 or Mp3 \033[37m:\033[93m ")
        if inp != "mp4" and inp != "mp3":
            print("\033[91m\033[01mYou must choose between Mp4 or Mp3!")
    if inp == "mp4":   
        for video in my_playlist.videos:
            try:
                video.register_on_progress_callback(playlist)
                video_filter_mp4 = re.sub('[^A-Za-z0-9]+','_', video.title)
                video.streams.get_highest_resolution()
                video.streams.filter(adaptive=True, file_extension='mp4').first().download(filename=''+video_filter_mp4+'.mp4')
                video.register_on_progress_callback(playlist)
                video_filter_mp3 = re.sub('[^A-Za-z0-9]+','_', video.title)
                video.streams.get_highest_resolution()
                video.streams.filter(only_audio=True, file_extension='webm').first().download(filename=''+video_filter_mp3+'.mp3')
                os.system('ffmpeg -hide_banner -loglevel error -i '+video_filter_mp4+'.mp4 -i '+video_filter_mp3+'.mp3 -c:v copy -c:a aac '+video_filter_mp4+'_ffmpeg.mp4')
                os.system('rm '+video_filter_mp4+'.mp4')
                os.system('mv '+video_filter_mp4+'_ffmpeg.mp4 '+video_filter_mp4+'.mp4')
                os.system('rm '+video_filter_mp3+'.mp3')
            except:
                pass
        print("")
        print("\033[92mDownload Done!")
        print("\033[37m")
        my_playlist_filter = re.sub('[^A-Za-z0-9]+','_', my_playlist.title)
        os.system('zip '+my_playlist_filter+'.zip *.mp4')
        os.system('cp '+my_playlist_filter+'.zip /var/www/html')
        os.system('rm '+my_playlist_filter+'.zip')
        print("")
        os.system('rm *.mp4')
        print('')
        print('\033[92mDownload Link \033[37m: \033[93mhttp://'+myip+'/'+my_video_filter+'.zip')
        print('')
    if inp == "mp3":
        for video in my_playlist.videos:
            video.register_on_progress_callback(playlist)
            video_filter_webm = re.sub('[^A-Za-z0-9]+','_', video.title)
            video.streams.get_highest_resolution()
            video.streams.filter(only_audio=True, file_extension='webm').first().download(filename=''+video_filter_webm+'.mp3')
        print("")
        print("\033[92mDownload Done!")
        print("\033[37m")
        my_playlist_filter = re.sub('[^A-Za-z0-9]+','_', my_playlist.title)
        os.system('zip '+my_playlist_filter+'.zip *.mp3')
        os.system('cp '+my_playlist_filter+'.zip /var/www/html')
        os.system('rm '+my_playlist_filter+'.zip')
        print("")
        os.system('rm *.mp3')
        print('')
        print('\033[92mDownload Link \033[37m: \033[93mhttp://'+myip+'/'+my_playlist_filter+'.zip')
        print('')
if question == "2":
    print("")
    vid = input("\033[92mEnter Youtube Video Url \033[37m: \033[93m")
    my_video = YouTube(vid, on_progress_callback=vids)
    lst = []
    print("")
    print("Calculating Playlist Length...")
    numbers = int(my_video.length)
    lst.append(numbers)
    length = (sum(lst)/60)
    print('\033[92mPlaylist Length \033[37m: \033[93m{} Minutes - ( {} )'.format(round(length),length))
    inp = ""
    while inp != "mp4" and inp != "mp3":
        print("")
        inp = input("\033[92mDownload Mp4 or Mp3 \033[37m:\033[93m ")
        if inp != "mp4" and inp != "mp3":
            print("\033[91m\033[01mYou must choose between Mp4 or Mp3!")
    if inp == "mp4":
        #my_video_filter = re.sub('[^A-Za-z0-9]+','_', my_video.title)
        #my_video.streams.get_highest_resolution()
        #my_video.streams.filter(progressive='true', file_extension='mp4').first().download(filename=''+my_video_filter+'.mp4')
        my_video.register_on_progress_callback(vids)
        my_video_filter_mp4 = re.sub('[^A-Za-z0-9]+','_', my_video.title)
        my_video.streams.get_highest_resolution()
        my_video.streams.filter(adaptive=True, file_extension='mp4').first().download(filename=''+my_video_filter_mp4+'.mp4')
        my_video.register_on_progress_callback(vids)
        my_video_filter_mp3 = re.sub('[^A-Za-z0-9]+','_', my_video.title)
        my_video.streams.get_highest_resolution()
        my_video.streams.filter(only_audio=True, file_extension='webm').first().download(filename=''+my_video_filter_mp3+'.mp3')
        os.system('ffmpeg -hide_banner -loglevel error -i '+my_video_filter_mp4+'.mp4 -i '+my_video_filter_mp3+'.mp3 -c:v copy -c:a aac '+my_video_filter_mp4+'_ffmpeg.mp4')
        os.system('rm '+my_video_filter_mp4+'.mp4')
        os.system('mv '+my_video_filter_mp4+'_ffmpeg.mp4 '+my_video_filter_mp4+'.mp4')
        os.system('rm '+my_video_filter_mp3+'.mp3')
        os.system('cp '+my_video_filter_mp4+'.mp4 /var/www/html')
        os.system("rm '"+my_video_filter_mp4+".mp4'")
        print("")
        print('\033[92mDownload Done!')
        print('')
        print('\033[92mDownload Link \033[37m: \033[93mhttp://'+myip+'/'+my_video_filter_mp4+'.mp4')
        print('')
        if click.confirm('\033[31mDelete Download Link?', default=True):
            os.system("cd /var/www/html && rm '"+my_video_filter_mp4+".mp4'")
            print("")
            print('\033[92mDone!\033[0m')
        print("\033[0m")
    if inp == "mp3":
        my_video_filter = re.sub('[^A-Za-z0-9]+','_', my_video.title)
        my_video.streams.get_highest_resolution()
        my_video.streams.filter(only_audio=True, file_extension='webm').first().download(filename=''+my_video_filter+'.mp3')
        os.system('cp '+my_video_filter+'.mp3 /var/www/html')
        os.system("rm '"+my_video_filter+".mp3'")
        print("")
        print('\033[92mDownload Done!')
        print('')
        print('\033[92mDownload Link \033[37m: \033[93mhttp://'+myip+'/'+my_video_filter+'.mp3')
        print('')
        if click.confirm('\033[31mDelete Download Link?', default=True):
            os.system("cd /var/www/html && rm '"+my_video_filter+".mp3'")
            print("")
            print('\033[92mDone!\033[0m')
        print("\033[0m")
if question == "3":
    print("")
    url = input("\033[92mEnter File That You Want To Download \033[37m: \033[93m")
    print("")
    basename = os.path.basename(url)
    basename_filter = re.sub('[^A-Za-z0-9]+','_', basename)
    os.system("clear")
    print("\033[92mDownloading \033[37m: \033[93m" + basename)
    wget.download(url, bar=wget_bar)
    os.system('cp '+basename+' /var/www/html')
    os.system('rm ' + basename)
    print('')
    print('\033[92mDownload Link \033[37m: \033[93mhttp://'+myip+'/' + basename)
    print('')
    if click.confirm('\033[31mDelete Download Link?', default=True):
        os.system('cd /var/www/html && rm ' + basename)
        print("")
        print('\033[92mDone!')
    print("\033[0m")
if question == "x":
    print("\033[0m")
    print("")
    print("Goodbye...")
    print("")
    exit
