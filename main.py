from tkinter import *
import tkinter as tk
from tkinter import ttk
from pytube import YouTube
from tkinter import filedialog, messagebox
from tkinter.messagebox import showinfo
ydl_opts = {
        'format': 'bestaudio/best',
        'extractaudio': True,
        'audioformat': 'mp3',
        'outtmpl': '%(title)s.f%(format_id)s.%(ext)s',
        'ignoreerrors': False,
        'noplaylist': True,
        'restrictfilenames': True,
    }
def createWidgets():
    link_label = Label(root, text="YutubeURL:", bg="#03c9ff")
    link_label.grid(row=1, column=0, pady=1, padx=30, )
    root.link_text= Entry(root,width=60,textvariable=video_link)
    root.link_text.grid(row=2,column=0,pady=1,padx=30)
    ziel_label=Label(root,text="Ziel",bg="#03c9ff")
    ziel_label.grid(row=3, column=0, pady=1, padx=30)
    root.ziel_text=Entry(root,width=60,textvariable=download_path)
    root.ziel_text.grid(row=4, column=0, pady=1, padx=30)
    browse_but=Button(root,text="Browse",command=browse,width=25,bg="#00ff04")
    browse_but.grid(row=5, column=0, pady=1, padx=30)
    downloadmp4_but=Button(root,text="Download Video",command=mp4,width=25,bg="#00ff04")
    downloadmp4_but.grid(row=6, column=0,pady=1,padx=30)
    downloadmp3_but = Button(root, text="Download Audio", command=mp3, width=25, bg="#00ff04")
    downloadmp3_but.grid(row=7, column=0, pady=1, padx=30)
def browse():
    download_dir=filedialog.askdirectory(initialdir="your Directory Path")
    download_path.set(download_dir)
def mp4():
    url=video_link.get()
    folder=download_path.get()
    get_video=YouTube(url)
    get_stream=get_video.streams.get_highest_resolution()
    get_stream.download(folder)
    messagebox.showinfo("Erfolgreich Abgeschlossen","Der Download wurde Erfolgreich Abgeschlossen du findest dein video in\n"+folder)
def mp3():
    url=video_link.get()
    folder=download_path.get()
    get_video=YouTube(url)
    get_stream = get_video.streams.get_highest_resolution()
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    messagebox.showinfo("Erfolgreich Abgeschlossen","Der Download wurde Erfolgreich Abgeschlossen du findest dein video in\n"+folder)
root = tk.Tk()
root.geometry("420x190")
root.resizable(False,False)
root.title("Youtube Downloader")
root.config(background="#03c9ff")
video_link=StringVar()
download_path=StringVar()
createWidgets()
root.mainloop()
print("Der Youtube Downloader wurde Beendet")
