import tkMessageBox
import ttk
from Tkinter import *
from PIL import Image, ImageTk

from scraper.tooltip import CreateToolTip
from scraper.web2 import page1
import socket

from scraper.web3 import wet


class home:
    def but1(self,event):
        try:
            socket.create_connection(("www.google.com", 80))
            n = page1(self.root)
        except:
            msg=tkMessageBox.showerror("NO CONNECTION", "You are not connected to the internet. Please check your connection and try again!!")

    def but2(self,event):

        try:
            socket.create_connection(("www.google.com", 80))
            n = wet(self.root)
        except:
            msg=tkMessageBox.showerror("NO CONNECTION", "You are not connected to the internet. Please check your connection and try again!!")


    # def but3(self,event):
    #     self.tv.configure(text="The TV shows you love!!")
    #
    # def but4(self,event):
    #     self.mus.configure(text="Music you may wanna hear")

    def __init__(self):
        self.root = Tk()
        self.root.minsize(width=700, height=400)
        self.root.maxsize(width=700, height=400)
        self.root.title("Scraper")
        self.root.iconbitmap('webscrape.ico')
        im = Image.open('back2.jpg')
        tkimage = ImageTk.PhotoImage(im)
        myvar = Label(self.root, image=tkimage)
        myvar.place(x=0, y=0, relwidth=1, relheight=1)
        myvar.image=tkimage
        nw = Image.open('news.jpg')
        tkimage1 = ImageTk.PhotoImage(nw)

        wt = Image.open('weather.jpg')
        tkimage2 = ImageTk.PhotoImage(wt)

        tvs = Image.open('tv.jpg')
        tkimage3 = ImageTk.PhotoImage(tvs)

        music = Image.open('music.jpg')
        tkimage4 = ImageTk.PhotoImage(music)

        style = ttk.Style()
        style.configure("TButton", relief="flat", background="#ccc", width=30, height=10)

        news = ttk.Button(self.root, style="TButton", image=tkimage1)
        news.image=tkimage1
        nstp = CreateToolTip(news, "Get the latest News updates from around the world!")
        news.bind('<Button-1>', self.but1)
        news.place(x=70, y=120)

        self.weather = ttk.Button(self.root, style="TButton", image=tkimage2)
        self.weather.image=tkimage2
        self.weather.place(x=430, y=120)
        wtp = CreateToolTip(self.weather, "Get the latest Weather updates in your area!")
        self.weather.bind('<Button-1>', self.but2)

        # self.tv = ttk.Button(self.root, style="TButton", image=tkimage3)
        # self.tv.image=tkimage3
        # tvtp = CreateToolTip(self.tv, "The TV shows you love!!")
        # self.tv.place(x=70, y=220)
        # self.tv.bind('<Button-1>', self.but3)
        #
        # self.mus = ttk.Button(self.root, style="TButton", image=tkimage4)
        # self.mus.image=tkimage4
        # mtp = CreateToolTip(self.mus, "Music you may wanna hear")
        # self.mus.place(x=430, y=220)
        # self.mus.bind('<Button-1>', self.but4)


if __name__ == "__main__":
    a=home()
    a.root.mainloop()
    exit(0)

