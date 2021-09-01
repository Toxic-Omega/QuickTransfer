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

myip = subprocess.getoutput("hostname -i")

def playlist(stream, chunk, bytes_remaining):
    os.system("clear")
    print("" + quicktransfer)
    print('\033[92mDownloading \033[37m: \033[93m' + my_playlist.title)
    print('\033[92mVideos \033[37m:\033[93m %s' % len(my_playlist.video_urls))
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
    ply = input("\033[92mEnter Youtube Playlist Url \033[37m:\033[93m ")
    my_playlist = Playlist(ply)
    for video in my_playlist.videos:
        video.register_on_progress_callback(playlist)
        video.streams.filter(type='video', progressive=True, file_extension='mp4').first().download('')
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
    print('\033[92mDownload Link \033[37m: \033[93mhttp://'+myip+'/'+my_playlist_filter+'.zip')
    print('')
    if click.confirm('\033[31mDelete Download Link?', default=True):
        os.system('cd /var/www/html && rm '+my_playlist_filter+'.zip')
        print("")
        print('\033[92mDone!\033[0m')
    print("\033[0m")
if question == "2":
    print("")
    vid = input("\033[92mEnter Youtube Video Url \033[37m: \033[93m")
    my_video = YouTube(vid, on_progress_callback=vids)
    my_video = my_video.streams.get_highest_resolution()
    my_video_filter = re.sub('[^A-Za-z0-9]+','_', my_video.title)
    my_video.download(filename=''+my_video_filter+'.mp4')
    os.system('cp '+my_video_filter+'.mp4 /var/www/html')
    os.system("rm '"+my_video_filter+".mp4'")
    print("")
    print('\033[92mDownload Done!')
    print('')
    print('\033[92mDownload Link \033[37m: \033[93mhttp://'+myip+'/'+my_video_filter+'.mp4')
    print('')
    if click.confirm('\033[31mDelete Download Link?', default=True):
        os.system("cd /var/www/html && rm '"+my_video_filter+".mp4'")
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
