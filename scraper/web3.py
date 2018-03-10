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
import geocoder

url1="https://weather.com/weather/today/l/"
url2="?par=google"
div=[]
class wet:
    def __init__(self,root):
        self.root=root
        self.root.minsize(width=910, height=600)
        self.v = IntVar()

        self.im1 = Image.open('back2.jpg')
        self.page1image = ImageTk.PhotoImage(self.im1)

        self.lab = Label(self.root, image=self.page1image)
        self.lab.image = self.page1image
        self.lab.place(x=0, y=0, relwidth=1, relheight=1)
        self.can = Canvas(self.root, background="lightblue")

        self.frame = Frame(self.can)
        canvas_id = self.can.create_text(390, 300, font=("Monotype Corsiva", 34), anchor="center")

        self.can.itemconfig(canvas_id, text="To view the weather please click \non get weather")

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

    def goweb1(self):
        webbrowser.open("https://weather.com"+div[0])
    def goweb2(self):
        webbrowser.open("https://weather.com"+div[1])
    def getwet(self):

        # try:
            g = geocoder.ip('me')
            latitude = str(g.lat)
            longitude = str(g.lng)
            os.system('cls')
            for widget in self.frame.winfo_children():
                widget.destroy()
            code = urllib2.urlopen(url1 + latitude + "," + longitude + url2)
            soup = BeautifulSoup(code, "html.parser")
            count = 0
            j = 0
            fon2 = tkFont.Font(family='Times New Roman', size=18, weight='bold')
            fon3 = tkFont.Font(family='Arial', size=12, weight='bold')
            # rn=[]
            # rntemp=[]
            for title in soup.find('div', class_="today_nowcard"):

                loc = title.find('h1', class_="h4 today_nowcard-location")
                print loc.text
                ti = title.find('p', class_="today_nowcard-timestamp")
                print ti.text
                temp = title.find('div', class_="today_nowcard-temp")
                print temp.text
                type=title.find('div', class_="today_nowcard-phrase")
                print type.text
                feel=title.find('div', class_="today_nowcard-feels")
                print feel.text
                uv = title.find('div', class_="today_nowcard-hilo")
                print uv.find('div').text
                now = title.find('div', class_="today_nowcard-sidecar component panel")
                for i in now.find_all('tr'):
                    print i.find("th").text, " ",

                    print i.find("td").text

                    l2 = Label(self.frame, text=i.find("th").text+"\n"+i.find("td").text
                               , width=30, wraplength=250
                               , justify=CENTER, font=fon3
                               , background='gray',fg="blue"
                               )
                    l2.grid(row=count, column=3,columnspan=2)
                    count+=1
            l1 = Label(self.frame, text=loc.text + "\n\n" + ti.text+ "\n\n" + temp.text+" F"+"\n\n" + type.text+
                                        "\n\n" + feel.text+" F"+ "\n\n" + uv.find('div').text
                          , width=30, wraplength=250
                          , justify=CENTER, font=fon2
                          , background='lightgreen',fg="brown"   )
            l1.grid(row=0, column=0, rowspan=5,columnspan=3,sticky=W+E+N+S)

            but = soup.find('div', class_="card card-padding")
            hr=but.find('a',class_="cta-link")
            div.append(hr.get('href'))
            td=but.find('a',class_="cta-link last-link")
            div.append(td.get('href'))
            card = soup.find('div', class_="looking-ahead")
            day1 = card.find('div', class_="today-daypart-content")

            d0=[]
            for y in day1.find_all('span'):
                print y.text
                d0.append(y.text)
            l3 = Label(self.frame, text=d0[0]+"\n\n"+d0[1]+"\n\n"+d0[2]+"F\n\n"+"Precipitation:"+"\n"+ d0[4]
               , width=14, wraplength=250
               , justify=CENTER, font=fon3
               , background='blue', fg="white",
               )
            l3.grid(row=count, column=0)

            d1=[]
            day2 = card.find('div', class_="today-daypart daypart-1")
            for y in day2.find_all('span'):
                print y.text
                d1.append(y.text)

            l4 = Label(self.frame, text=d1[0] + "\n\n" + d1[1] + "\n\n" + d1[2] + "F\n\n" + "Precipitation:" + "\n"+ d1[4]
               , width=14, wraplength=250
               , justify=CENTER, font=fon3
               , background='blue', fg="white",
               )
            l4.grid(row=count, column=1)

            d2=[]
            day3 = card.find('div', class_="today-daypart daypart-2")
            for y in day3.find_all('span'):
                print y.text
                d2.append(y.text)
            l5 = Label(self.frame, text=d2[0] + "\n\n" + d2[1] + "\n\n" + d2[2] + "F\n\n" + "Precipitation:"+ "\n"+ d2[4]
               , width=14, wraplength=250
               , justify=CENTER, font=fon3
               , background='blue', fg="white",
               )
            l5.grid(row=count, column=2)

            d3=[]
            day4 = card.find('div', class_="today-daypart daypart-3")
            for y in day4.find_all('span'):
                print y.text
                d3.append(y.text)
            l6 = Label(self.frame, text=d3[0] + "\n\n" + d3[1] + "\n\n" + d3[2] + "F\n\n" + "Precipitation:" + "\n"+ d3[4]
               , width=15, wraplength=250
               , justify=CENTER, font=fon3
               , background='blue', fg="white",
               )
            l6.grid(row=count, column=3)

            d4=[]
            day5 = card.find('div', class_="today-daypart daypart-4")
            for y in day5.find_all('span'):
                print y.text
                d4.append(y.text)
            l7 = Label(self.frame, text=d4[0] + "\n\n" + d4[1] + "\n\n" + d4[2] + "F\n\n" + "Precipitation:" + "\n"+ d4[4]
                           , width=15, wraplength=250
                           , justify=CENTER, font=fon3
                           , background='blue', fg="white",
                           )
            l7.grid(row=count, column=4)
            count+=1


            h = ttk.Button(self.can, text="Hourly \n Report->",
                   style="TButton",
                   compound=LEFT,command=self.goweb1)
            h.place(x=70, y=500)

            n10 = ttk.Button(self.can, text="10 Days \nReport->",
                   style="TButton",
                   compound=LEFT, command=self.goweb2)
            n10.place(x=500, y=500)

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
        h = home()

    def open(self):



        fon3 = tkFont.Font(family='Times New Roman', size=12, weight='bold')
        ttk.Style().configure("TButton", width=10, font=fon3, foreground='darkgreen')
        test = Image.open('wet1.png')
        radioimg = ImageTk.PhotoImage(test)

        temp = ttk.Button(self.root,
                                   style="TButton",

                                   text="Get Weather",

                                   command=self.getwet,

                                   image=radioimg,
                                   compound=LEFT
                                   )
        temp.image = radioimg
        temp.pack(anchor=W,padx=10,pady=30)

        temp.image = radioimg
        r = Image.open('ref.png')
        ref = ImageTk.PhotoImage(r)

        refresh = ttk.Button(self.root, text="REFRESH",
                             style="TButton", image=ref,
                             compound=LEFT, command=self.getwet)
        refresh.image = ref
        refresh.pack(anchor='center', padx=10,pady=30)
        r = Image.open('home.png')
        home = ImageTk.PhotoImage(r)
        h = ttk.Button(self.root, text="BACK",
                       style="TButton", image=home,
                       compound=LEFT, command=self.back)
        h.image = home
        h.pack(anchor='center',padx=10 ,pady=30)
