from pytube import YouTube
from pytube import Playlist
import os
import sys
import subprocess
import click
import wget
import os.path
import re

myip = subprocess.getoutput("hostname -i")

#hippity hoppity your code is now my property
def playlist(stream, chunk, bytes_remaining):
    os.system("clear")
    print("\033[92mDownloading \033[37m: \033[93m" + my_playlist.title)
    print('\033[92mVideos \033[37m:\033[93m %s' % len(my_playlist.video_urls))
    curr = stream.filesize - bytes_remaining
    done = int(50 * curr / stream.filesize)
    sys.stdout.write("\r\033[37m[ {}{}\033[37m ] ".format('\033[94mX' * done, ' ' * (50-done)) )
    sys.stdout.flush()
    print("\033[93m" + video.title)

#hippity hoppity your code is now my property
def vids(stream, chunk, bytes_remaining):
    os.system("clear")
    print("\033[92mDownloading\033[37m :\033[93m " + my_video.title)
    curr = stream.filesize - bytes_remaining
    done = int(50 * curr / stream.filesize)
    sys.stdout.write("\r\033[37m[ {}{}\033[37m ] ".format('\033[94mX' * done, ' ' * (50-done)) )
    sys.stdout.flush()
    print("\033[93m" + my_video.title)

os.system("clear")
print("""
\033[91m _____       _      _    _                        __          
|  _  |     (_)    | |  | |                      / _|         
| | | |_   _ _  ___| | _| |_ _ __ __ _ _ __  ___| |_ ___ _ __ 
| | | | | | | |/ __| |/ / __| '__/ _` | '_ \/ __|  _/ _ \ '__|
\ \/' / |_| | | (__|   <| |_| | | (_| | | | \__ \ ||  __/ |   
 \_/\_\\__,_|_|\___|_|\_\\__|_|  \__,_|_| |_|___/_| \___|_|   
                                                              
\033[37m[ \033[31m1 \033[37m]  Youtube Playlist
\033[37m[ \033[31m2 \033[37m]  Youtube Video            \033[92mWhat Do You Want To Download?
\033[37m[ \033[31m3 \033[37m]  Other File
\033[37m[ \033[31mx \033[37m]  Exit
""")
question = input("\033[92mSelect \033[37m:\033[93m ")

if question == "1":
    print("")
    ply = input("\033[92mEnter Youtube Playlist Url \033[37m:\033[93m ")
    my_playlist = Playlist(ply)
    #hippity hoppity your code is now my property
    for video in my_playlist.videos:
        try:
            stream = video.streams.get_by_itag(137)
            video.register_on_progress_callback(playlist)
            stream.download()
        except AttributeError:
            stream = video.streams.get_by_itag(22)
            video.register_on_progress_callback(playlist)
            stream.download()
        except:
            print("\033[91mSomething went wrong.")
    print("")
    print("\033[92mDownload Done!")
    print("\033[37m")
    os.system('zip '+my_playlist.title+'.zip *.mp4')
    os.system('cp '+my_playlist.title+'.zip /var/www/html')
    os.system('rm '+my_playlist.title+'.zip')
    print("")
    os.system('rm *.mp4')
    print('')
    print('\033[92mDownload Link \033[37m: \033[93mhttp://'+myip+'/'+my_playlist.title+'.zip')
    print('')
    if click.confirm('\033[31mDelete Download Link?', default=True):
        os.system('cd /var/www/html && rm '+my_playlist.title+'.zip')
        print('\033[92mDone!\033[0m')
    print("\033[0m")
if question == "2":
    print("")
    vid = input("\033[92mEnter Youtube Video Url \033[93m: \033[92m")
    my_video = YouTube(vid, on_progress_callback=vids)
    my_video = my_video.streams.get_highest_resolution()
    my_video_filter = re.sub("[^a-zA-Z]+", "", "" + my_video.title)
    my_video.download(filename=''+my_video_filter+'.mp4')
    os.system('cp '+my_video_filter+'.mp4 /var/www/html')
    os.system("rm '"+my_video_filter+".mp4'")
    print('\033[92mDownload Done!')
    print('')
    print('\033[92mDownload Link \033[37m: \033[93mhttp://'+myip+'/'+my_video_filter+'.mp4')
    print('')
    if click.confirm('\033[31mDelete Download Link?', default=True):
        os.system("cd /var/www/html && rm '"+my_video_filter+".mp4'")
        print('\033[92mDone!\033[0m')
    print("\033[0m")
if question == "3":
    url = input("\033[92mEnter File That You Want To Download \033[37m: \033[93m")
    basename = os.path.basename(url)
    print("\033[92mDownloading...")
    wget.download(url)
    os.system('cp '+basename+' /var/www/html')
    os.system('rm ' + basename)
    print('')
    print('')
    print('\033[92mDownload Link \033[37m: \033[93mhttp://'+myip+'/' + basename)
    print('')
    if click.confirm('\033[31mDelete Download Link?', default=True):
        os.system('cd /var/www/html && rm ' + basename)
        print('\033[92mDone!')
    print("\033[0m")
if question == "x":
    print("\033[0m")
    exit
