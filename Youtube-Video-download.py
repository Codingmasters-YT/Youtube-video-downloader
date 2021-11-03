from  tkinter import *

from pytube import YouTube
root = Tk()
root.geometry('500x300')
root.resizable(0 , 0)
root.title("Video downloader")

Headindg = Label(text = "Paste the link" , font = 'arial 15 bold')

link = StringVar()

Label(root, text = 'Paste Link Here:', font = 'arial 15 bold').place(x= 160 , y = 60)
link_enter = Entry(root, width = 70,textvariable = link).place(x = 32, y = 90)

def Downloader():     
    url =YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    Label(root, text = 'DOWNLOADED', font = 'arial 15').place(x= 180 , y = 210)


btn = Button(text = "Downlaod"  , height = "2" , width = "12",bg = "pink" , command = Downloader).place(x=200 , y = 150 )





# Headindg.pack()
# enter.pack()
# btn.pack()
root.mainloop()
