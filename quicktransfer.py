import os
from pytube import YouTube
from pytube.cli import on_progress
import sys
import subprocess
import click
import wget
import os.path

os.system("apt update && apt upgrade -y")
os.system("apt install rename -y")
os.system("clear")
print("(1)  Youtube Video")
print("(2)  Other File")
print("")
print("What Are You Downloading?")
print("")
question = input("Select : ")

if question == "1":
    print("")
    url = input("Enter Youtube Video Url : ")

    #hippity hoppity your code is now my property
    def progress_func(stream, chunk, bytes_remaining):
        curr = stream.filesize - bytes_remaining
        done = int(50 * curr / stream.filesize)
        sys.stdout.write("\r[{}{}] ".format('=' * done, ' ' * (50-done)) )
        sys.stdout.flush()
    
    my_video = YouTube(url, on_progress_callback=progress_func)
    print("Downloading : " + my_video.title)
    my_video = my_video.streams.get_highest_resolution()
    my_video.download()
    os.system('rename "s/ /_/g" *')
    os.system('cp *.mp4 /var/www/html')
    os.system('rm *.mp4')
    os.system('clear')
    print('Download Done!')
    output = subprocess.getoutput("cd /var/www/html && ls | egrep '\.mp4$'")
    print('')
    print('Download Link : http://192.168.1.69/' + output)
    print('')
    if click.confirm('Delete Download Link?', default=True):
        os.system('cd /var/www/html && rm *.mp4')
        print('Done!')
    if click.confirm('Shutdown ProxMox?', default=True):
        os.system('bash hs100.sh -i 192.168.1.19 off && poweroff')
        print('Done!')
if question == "2":
    url = input("Enter File That You Want To Download : ")
    basename = os.path.basename(url)
    print("Downloading...")
    wget.download(url)
    os.system('cp '+basename+' /var/www/html')
    os.system('rm ' + basename)
    print('')
    print('')
    print('Download Link : http://192.168.1.69/' + basename)
    print('')
    if click.confirm('Delete Download Link?', default=True):
        os.system('cd /var/www/html && rm ' + basename)
        print('Done!')
    if click.confirm('Shutdown ProxMox?', default=True):
        os.system('bash hs100.sh -i 192.168.1.19 off && poweroff')
        print('Done!')
