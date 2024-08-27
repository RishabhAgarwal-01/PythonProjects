import yt_dlp
import tkinter as tk
from tkinter import filedialog

def download_video(url, save_path):
    ydl_opts = {
        'outtmpl': f'{save_path}/%(title)s.%(ext)s',
        'format': 'best',
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("Video downloaded successfully")
    except Exception as e:
        print(f"An error occurred: {e}")

def open_file_dialog():
    folder = filedialog.askdirectory()
    if folder:
        print(f"Selected Folder {folder}")
    return folder


if __name__ == '__main__':
    root = tk.Tk()
    root.withdraw()
    video_url = input("Please enter a Youtube url: ")
    save_dir = open_file_dialog()
    if not save_dir:
        print("Please select the folder")
    else:
        print("Started download")
        download_video(video_url,save_dir)
        print("Download Finish")
