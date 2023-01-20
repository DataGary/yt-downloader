from pytube import Playlist
from pytube import YouTube
import tkinter as tk
from tkinter import filedialog

print("Select download folder: ")

root = tk.Tk()
root.withdraw()

selected_directory = filedialog.askdirectory()

print(f'Selected download folder: {selected_directory}')

def on_progress(vid, chunk, bytes_remaining):
    total_size = vid.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    totalsz = (total_size/1024)/1024
    totalsz = round(totalsz,1)
    remain = (bytes_remaining / 1024) / 1024
    remain = round(remain, 1)
    dwnd = (bytes_downloaded / 1024) / 1024
    dwnd = round(dwnd, 1)
    percentage_of_completion = round(percentage_of_completion,2)

    #print(f'Total Size: {totalsz} MB')
    print(f'Download Progress: {percentage_of_completion}%, Total Size:{totalsz} MB, Downloaded: {dwnd} MB, Remaining:{remain} MB')

print("--------Youtube Downloader---------")
try:
    sel = input("Type v for single video download or p for playlist download: ")
except ValueError:
    print("Select v or p")

if sel == "v":
    link = input("Paste the link to the YouTube video: ")

    yt = YouTube(link)
    yt.register_on_progress_callback(on_progress)

    print("Title: ", yt.title)
    print("Views: ", yt.views)

    yd = yt.streams.get_highest_resolution()

    print("Downloading...")
    yd.download(selected_directory)
    print("Download complete!")

elif sel == "p":
    link = input("Paste the link to the YouTube playlist: ")

    play_list = Playlist(link)

    print("Playlist title: ", play_list.title)
    print("Playlist views: ", play_list.views)

    # output folder
    dl_folder = selected_directory
    for video in play_list.videos:
        print(f'Downloading: {video.title}')
        video.register_on_progress_callback(on_progress)
        video.streams.get_highest_resolution().download(dl_folder)

    print('Downloads complete!')

else:
    print('Select "v" for single video download or "p" for playlist download.')