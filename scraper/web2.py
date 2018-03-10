from bs4 import BeautifulSoup
import urllib2
import ttk
from Tkinter import *
from PIL import Image, ImageTk
import tkFont
import os
import io
import threading
import webbrowser



global im1,page1image,nw,tkimage1

types=[("Top Stories",'note1.png',1),("India",'flag.png',2),("World",'globe.png',3),("Business",'busi.png',4),
       ("Technology",'tech.png',5),("Entertainment",'entr.png',6),
       ("Sports",'sport.png',7),("Science",'sci.png',8),("Health",'heal.png',9)]
url=None

div=[]




class page1:
    def __init__(self,root):
        self.root=root
        self.root.minsize(width=900, height=600)
        self.v=IntVar()

        self.im1 = Image.open('back2.jpg')
        self.page1image = ImageTk.PhotoImage(self.im1)

        self.lab = Label(self.root, image=self.page1image)
        self.lab.image = self.page1image
        self.lab.place(x=0, y=0, relwidth=1, relheight=1)
        self.can = Canvas(self.root,background="lightblue")

        self.frame = Frame(self.can)
        canvas_id = self.can.create_text(300, 300,font=("Monotype Corsiva",34) ,anchor="center")

        self.can.itemconfig(canvas_id, text="To view the news please select \none of the categories from the list")

        self.scroll = Scrollbar(self.root, orient="vertical", command=self.can.yview)
        self.can.configure(yscrollcommand=self.scroll.set)
        self.scroll.pack(side=RIGHT, fill=Y)
        # self.can.place(x=237, y=0)
        self.can.pack(side="right", fill="both", expand=True)

        self.can.create_window((4, 4), window=self.frame, anchor="nw", tags="self.frame")

        self.frame.bind("<Configure>", lambda x: self.can.configure(scrollregion=self.can.bbox("all")))
        self.root.bind("<Down>", lambda x: self.can.yview_scroll(3, 'units'))  # bind "Down" to scroll down
        self.root.bind("<Up>", lambda x: self.can.yview_scroll(-3, 'units'))  # bind "Up" to scroll up
        # bind the mousewheel to scroll up/down
        self.root.bind("<MouseWheel>", lambda x: self.can.yview_scroll(int(-1 * (x.delta / 40)), "units"))
        self.open()




    def goweb(self,event,ind):
        webbrowser.open(div[ind])

    def ShowChoice(self):

        # try:
            os.system('cls')
            for widget in self.frame.winfo_children():
                widget.destroy()

            if (self.v.get() == 1):
                # print 1
                url = "https://news.google.com/news/?ned=in&hl=en-IN"

                # code = urllib2.urlopen(url)
            elif (self.v.get() == 2):
                url = "https://news.google.com/news/headlines/section/topic/NATION.en_in/India?ned=in&hl=en-IN"
                # code = urllib2.urlopen(url)

            elif self.v.get() == 3:
                url = "https://news.google.com/news/headlines/section/topic/WORLD.en_in/World?ned=in&hl=en-IN"
                # code = urllib2.urlopen(url)
                # print 2
            elif (self.v.get() == 4):
                # print 2
                url = "https://news.google.com/news/headlines/section/topic/BUSINESS.en_in/Business?ned=in&hl=en-IN"
                # code = urllib2.urlopen(url)
            elif (self.v.get() == 5):
                # print 2
                url = "https://news.google.com/news/headlines/section/topic/TECHNOLOGY.en_in/Technology?ned=in&hl=en-IN"
                # code = urllib2.urlopen(url)
            elif (self.v.get() == 6):
                url = "https://news.google.com/news/headlines/section/topic/ENTERTAINMENT.en_in/Entertainment?ned=in&hl=en-IN"
                # code = urllib2.urlopen(url)
                # print 2
            elif (self.v.get() == 7):
                url = "https://news.google.com/news/headlines/section/topic/SPORTS.en_in/Sport?ned=in&hl=en-IN"
                # code = urllib2.urlopen(url)
                # print 2
            elif (self.v.get() == 8):
                url = "https://news.google.com/news/headlines/section/topic/SCIENCE.en_in/Science?ned=in&hl=en-IN"
                # code = urllib2.urlopen(url)
                # print 2
            elif (self.v.get() == 9):
                url = "https://news.google.com/news/headlines/section/topic/HEALTH.en_in/Health?ned=in&hl=en-IN"
                # code = urllib2.urlopen(url)
                # print 2

            code = urllib2.urlopen(url)

            i = 0
            j = 0

            soup = BeautifulSoup(code, "html.parser")
            list = []
            for title in soup.find_all('c-wiz', class_="lPV2Xe k3Pzib"):
                k = title.find('img', class_="lmFAjc")
                if (k == None):

                    list.append("noimage.png")
                else:
                    list.append(k.get('src'))
            for temp in list:
                if temp == "noimage.png":
                    pil_img = Image.open(temp)
                else:
                    try:

                        my_page = urllib2.urlopen(temp)
                        # create an image file object
                        my_picture = io.BytesIO(my_page.read())
                        # use PIL to open image formats like .jpg  .png  .gif  etc.
                        pil_img = Image.open(my_picture)
                        my_page.close()
                    except:
                        pil_img = Image.open("noimage.png")
                # convert to an image Tkinter can use
                tk_img = ImageTk.PhotoImage(pil_img)
                # put the image on a typical widget
                label = Label(self.frame, image=tk_img)
                label.image = tk_img
                label.grid(row=j, column=0, rowspan=2)

                j += 2

            fon2 = tkFont.Font(family='Arial', size=12, weight='bold')
            fon3 = tkFont.Font(family='Arial', size=9, weight='bold')
            del div[:]
            ind = 0
            for title in soup.find_all('c-wiz', class_="M1Uqc kWyHVd"):
                temp = title.find('a')
                div.append(temp.get('href'))
                source = title.find('span', class_='IH8C7b Pc0Wt')
                time = title.find('span', class_='d5kXP YBZVLb')
                # print temp.get('href')
                # for i in range(4):

                l = Label(self.frame, text=temp.text, width=50, wraplength=350
                          , justify=LEFT, font=fon2
                          , background='gray',
                          )
                l.bind('<Button-1>', lambda event, ind=ind: self.goweb(event, ind))
                l.grid(row=i, column=1, sticky=W)
                l2 = Label(self.frame, text=source.text + "\n" + time.text, width=50, wraplength=350
                           , font=fon3, anchor='w')

                l2.grid(row=i + 1, column=1, sticky=W)

                # w = ttk.Separator(self.frame, orient=HORIZONTAL)
                # w.grid(row=i+2,colspan=3,sticky=W+E)
                i += 2
                ind += 1

        # except:
        #     master = Tk()
        #     whatever_you_do = "Either the category is not selected or there is a problem in internet connectivity! Please try again later"
        #     msg = Message(master, text=whatever_you_do)
        #     msg.config(bg='lightgreen', font=('times', 20, 'italic'))
        #     msg.pack()
        #     mainloop()


    def back(self):
        from scraper import home
        self.root.destroy()
        h=home()



    def open(self):

        i=0
        fon = tkFont.Font(family='Ariel', size=20, weight='bold')
        ttk.Style().configure("Toolbutton", padx=30, width=13, font=fon,foreground="#c39797 ")
        for txt, img,val in types:
            test = Image.open(img)
            radioimg = ImageTk.PhotoImage(test)

            temp=ttk.Radiobutton(self.root,
                            style="Toolbutton",

                        text=txt,
                        variable=self.v,
                        command=self.ShowChoice,
                        value=val,
                        image=radioimg,
                        compound=LEFT
                        )
            temp.image = radioimg
            temp.pack(anchor=W)
            i+=1
            temp.image=radioimg
        r=Image.open('ref.png')
        ref=ImageTk.PhotoImage(r)
        fon3=tkFont.Font(family='Times New Roman', size=12, weight='bold')
        ttk.Style().configure("TButton",width=10,font=fon3,foreground='darkgreen')
        refresh=ttk.Button(self.root,text="REFRESH",
                     style="TButton",image=ref,
                           compound=LEFT,command=self.ShowChoice)
        refresh.image=ref
        refresh.pack(anchor='center',pady=30)
        r = Image.open('home.png')
        home = ImageTk.PhotoImage(r)
        h = ttk.Button(self.root, text="BACK",
                             style="TButton", image=home,
                       compound=LEFT,command=self.back)
        h.image = home
        h.pack(anchor='center', pady=30)



# A=page1(root)
# root.mainloop()