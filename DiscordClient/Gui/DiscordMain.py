import tkinter as tk
from Gui import DiscordGroup, DiscordLogin
from Gui import DiscordJoin
from Gui import DiscordSubgroups
import threading


class Toplevel1:
    def __init__(self, sock, top, groups, username, online):
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        self.sock = sock
        self.top = top
        self.groupButtons = []
        self.subgroupButtons = []
        self.username = username
        self.online = online
        self.subgroup = ""
        self.messages = ''
        self.subgroups = None
        self.chat = None
        self.group = ""

        self.top.geometry("1498x790+249+225")
        self.top.minsize(120, 1)
        self.top.maxsize(1924, 1061)
        self.top.resizable(1,  1)
        self.top.title("Discord")
        self.top.configure(background="#36393f")
        self.top.configure(highlightbackground="#36393f")
        self.top.configure(highlightcolor="black")

        self.Frame1 = tk.Frame(self.top)
        self.Frame1.place(relx=0.0, rely=0.0, relheight=1.0, relwidth=0.052)
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#202125")
        self.Frame1.configure(highlightbackground="#28292e")
        self.Frame1.configure(highlightcolor="#28292e")
        self.Frame1.configure(highlightthickness="1")

        self.Button1 = tk.Button(self.Frame1)
        self.Button1.place(relx=0.192, rely=0.01, height=46, width=46)
        self.Button1.configure(activebackground="#5865f2")
        self.Button1.configure(activeforeground="white")
        self.Button1.configure(activeforeground="#ffffff")
        self.Button1.configure(background="#36393f")
        self.Button1.configure(borderwidth="0")
        self.Button1.configure(compound='left')
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#ffffff")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        photo_location = "Images/discordSign.png"
        global _img0
        _img0 = tk.PhotoImage(file=photo_location)
        self.Button1.configure(image=_img0)
        self.Button1.configure(pady="0")
        self.Button1.bind('<Button-1>', self.hideAll)

        self.Label2 = tk.Label(self.Frame1)
        self.Label2.place(relx=0.333, rely=0.1, height=2, width=27)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(anchor='w')
        self.Label2.configure(background="#313236")
        self.Label2.configure(compound='left')
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")

        self.Button1_1_1 = tk.Button(self.Frame1)
        self.Button1_1_1.place(relx=0.192, rely=0.88, height=46, width=46)
        self.Button1_1_1.configure(activebackground="#5865f2")
        self.Button1_1_1.configure(activeforeground="white")
        self.Button1_1_1.configure(activeforeground="#ffffff")
        self.Button1_1_1.configure(background="#36393f")
        self.Button1_1_1.configure(borderwidth="0")
        self.Button1_1_1.configure(compound='center')
        self.Button1_1_1.configure(disabledforeground="#a3a3a3")
        self.Button1_1_1.configure(font="-family {Segoe UI} -size 24 -weight bold")
        self.Button1_1_1.configure(foreground="#3ba55d")
        self.Button1_1_1.configure(highlightbackground="#d9d9d9")
        self.Button1_1_1.configure(highlightcolor="black")
        self.Button1_1_1.configure(highlightthickness="0")
        self.Button1_1_1.configure(padx="0")
        self.Button1_1_1.configure(pady="0")
        self.Button1_1_1.configure(relief="flat")
        self.Button1_1_1.configure(repeatdelay="-1")
        self.Button1_1_1.configure(repeatinterval="-1")
        self.Button1_1_1.configure(text='''+''')
        self.Button1_1_1.configure(wraplength="10000")
        self.Button1_1_1.bind('<Button-1>', self.addGroup)

        self.Button1_1_1_1 = tk.Button(self.Frame1)
        self.Button1_1_1_1.place(relx=0.192, rely=0.94, height=46, width=46)
        self.Button1_1_1_1.configure(activebackground="#5865f2")
        self.Button1_1_1_1.configure(activeforeground="white")
        self.Button1_1_1_1.configure(activeforeground="#000000")
        self.Button1_1_1_1.configure(background="#36393f")
        self.Button1_1_1_1.configure(borderwidth="0")
        self.Button1_1_1_1.configure(compound='left')
        self.Button1_1_1_1.configure(disabledforeground="#a3a3a3")
        self.Button1_1_1_1.configure(foreground="#ffffff")
        self.Button1_1_1_1.configure(highlightbackground="#d9d9d9")
        self.Button1_1_1_1.configure(highlightcolor="black")
        photo_location = "Images/search.png"
        global _img1
        _img1 = tk.PhotoImage(file=photo_location)
        self.Button1_1_1_1.configure(image=_img1)
        self.Button1_1_1_1.configure(pady="0")
        self.Button1_1_1_1.bind('<Button-1>', self.join)

        self.Frame2 = tk.Frame(self.top)
        self.Frame2.place(relx=0.052, rely=0.0, relheight=1.0, relwidth=0.16)
        self.Frame2.configure(relief="groove")
        self.Frame2.configure(background="#2f3035")
        self.Frame2.configure(highlightbackground="#d9d9d9")
        self.Frame2.configure(highlightcolor="black")

        self.Label3 = tk.Label(self.Frame2)
        self.Label3.place(relx=0.0, rely=0.065, height=2, width=240)
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(activeforeground="black")
        self.Label3.configure(anchor='w')
        self.Label3.configure(background="#25262b")
        self.Label3.configure(borderwidth="0")
        self.Label3.configure(compound='left')
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(highlightbackground="#25262b")
        self.Label3.configure(highlightcolor="#25262b")
        self.Label3.configure(highlightthickness="1")

        self.Frame5 = tk.Frame(self.Frame2)
        self.Frame5.place(relx=0.0, rely=0.925, relheight=0.075, relwidth=1.0)
        self.Frame5.configure(relief="groove")
        self.Frame5.configure(background="#2b2c31")
        self.Frame5.configure(highlightbackground="#d9d9d9")
        self.Frame5.configure(highlightcolor="black")

        self.Button7 = tk.Button(self.Frame5)
        self.Button7.place(relx=0.717, rely=0.323, height=24, width=27)
        self.Button7.configure(activebackground="#2b2c31")
        self.Button7.configure(activeforeground="#000000")
        self.Button7.configure(background="#2b2c31")
        self.Button7.configure(borderwidth="0")
        self.Button7.configure(compound='left')
        self.Button7.configure(disabledforeground="#a3a3a3")
        self.Button7.configure(foreground="#000000")
        self.Button7.configure(highlightbackground="#d9d9d9")
        self.Button7.configure(highlightcolor="black")
        photo_location = "Images/logout.png"
        global _img2
        _img2 = tk.PhotoImage(file=photo_location)
        self.Button7.configure(image=_img2)
        self.Button7.configure(pady="0")
        self.Button7.bind('<Button-1>', self.logout)


        self.Label7 = tk.Label(self.Frame5)
        self.Label7.place(relx=0.071, rely=0.254, height=30, width=29)
        self.Label7.configure(activebackground="#f9f9f9")
        self.Label7.configure(activeforeground="black")
        self.Label7.configure(anchor='center')
        self.Label7.configure(background="#1f2023")
        self.Label7.configure(borderwidth="0")
        self.Label7.configure(compound='left')
        self.Label7.configure(disabledforeground="#a3a3a3")
        self.Label7.configure(foreground="#ffffff")
        self.Label7.configure(highlightbackground="#d9d9d9")
        self.Label7.configure(highlightcolor="black")
        self.Label7.configure(font="-family {Segoe UI} -size 12 -weight bold")
        self.Label7.configure(text=username[0])

        self.Label8 = tk.Label(self.Frame5)
        self.Label8.place(relx=0.2, rely=0.254, height=16, width=100)
        self.Label8.configure(activebackground="#f9f9f9")
        self.Label8.configure(activeforeground="black")
        self.Label8.configure(anchor='w')
        self.Label8.configure(background="#2b2c31")
        self.Label8.configure(compound='left')
        self.Label8.configure(disabledforeground="#a3a3a3")
        self.Label8.configure(font="-family {Segoe UI} -size 10 -weight bold")
        self.Label8.configure(foreground="#ffffff")
        self.Label8.configure(highlightbackground="#d9d9d9")
        self.Label8.configure(highlightcolor="black")
        self.Label8.configure(text=username)

        self.Label3_1 = tk.Label(self.Frame2)
        self.Label3_1.place(relx=0.0, rely=0.066, height=2, width=240)
        self.Label3_1.configure(activebackground="#f9f9f9")
        self.Label3_1.configure(activeforeground="black")
        self.Label3_1.configure(anchor='w')
        self.Label3_1.configure(background="#2c2d32")
        self.Label3_1.configure(borderwidth="0")
        self.Label3_1.configure(compound='left')
        self.Label3_1.configure(disabledforeground="#a3a3a3")
        self.Label3_1.configure(foreground="#000000")
        self.Label3_1.configure(highlightbackground="#25262b")
        self.Label3_1.configure(highlightcolor="#25262b")
        self.Label3_1.configure(highlightthickness="1")

        self.Frame3 = tk.Frame(self.top)
        self.Frame3.place(relx=0.201, rely=0.0, relheight=1.0, relwidth=0.63)
        self.Frame3.configure(relief="groove")
        self.Frame3.configure(background="#363940")
        self.Frame3.configure(highlightbackground="#d9d9d9")
        self.Frame3.configure(highlightcolor="black")

        self.Label9 = tk.Label(self.Frame3)
        self.Label9.place(relx=0.0, rely=0.065, height=2, width=944)
        self.Label9.configure(activebackground="#f9f9f9")
        self.Label9.configure(activeforeground="black")
        self.Label9.configure(anchor='w')
        self.Label9.configure(background="#25262b")
        self.Label9.configure(borderwidth="0")
        self.Label9.configure(compound='left')
        self.Label9.configure(disabledforeground="#a3a3a3")
        self.Label9.configure(foreground="#000000")
        self.Label9.configure(highlightbackground="#33363b")
        self.Label9.configure(highlightcolor="#25262b")
        self.Label9.configure(padx="0")
        self.Label9.configure(pady="0")

        self.Frame4 = tk.Frame(self.top)
        self.Frame4.place(relx=0.83, rely=0.0, relheight=1.0, relwidth=0.262)
        self.Frame4.configure(relief="groove")
        self.Frame4.configure(background="#2f3035")
        self.Frame4.configure(highlightbackground="#d9d9d9")
        self.Frame4.configure(highlightcolor="black")

        self.Frame6 = tk.Frame(self.Frame4)
        self.Frame6.place(relx=0.0, rely=0.0, relheight=0.065, relwidth=1.0)
        self.Frame6.configure(relief="groove")
        self.Frame6.configure(background="#363940")
        self.Frame6.configure(highlightbackground="#d9d9d9")
        self.Frame6.configure(highlightcolor="black")

        self.Entry2 = tk.Entry(self.Frame6)
        self.Entry2.place(relx=0.219, rely=0.294, height=21, relwidth=0.298)
        self.Entry2.configure(background="#4a4d54")
        self.Entry2.configure(borderwidth="0")
        self.Entry2.configure(disabledforeground="#a3a3a3")
        self.Entry2.configure(font="TkFixedFont")
        self.Entry2.configure(foreground="#ffffff")
        self.Entry2.configure(highlightbackground="#d9d9d9")
        self.Entry2.configure(highlightcolor="black")
        self.Entry2.configure(insertbackground="#ffffff")
        self.Entry2.configure(selectbackground="blue")
        self.Entry2.configure(selectforeground="white")

        self.Label13 = tk.Label(self.Frame6)
        self.Label13.place(relx=0.501, rely=0.294, height=21, width=21)
        self.Label13.configure(activebackground="#f9f9f9")
        self.Label13.configure(activeforeground="black")
        self.Label13.configure(anchor='w')
        self.Label13.configure(background="#d9d9d9")
        self.Label13.configure(borderwidth="0")
        self.Label13.configure(compound='left')
        self.Label13.configure(disabledforeground="#a3a3a3")
        self.Label13.configure(foreground="#000000")
        self.Label13.configure(highlightbackground="#d9d9d9")
        self.Label13.configure(highlightcolor="black")
        photo_location = "Images/magnifying glass.png"
        global _img3
        _img3 = tk.PhotoImage(file=photo_location)
        self.Label13.configure(image=_img3)
        self.Label13.configure(padx="0")
        self.Label13.configure(pady="0")

        self.Label10 = tk.Label(self.Frame4)
        self.Label10.place(relx=0.0, rely=0.065, height=2, width=393)
        self.Label10.configure(activebackground="#f9f9f9")
        self.Label10.configure(activeforeground="black")
        self.Label10.configure(anchor='w')
        self.Label10.configure(background="#25262b")
        self.Label10.configure(compound='left')
        self.Label10.configure(disabledforeground="#a3a3a3")
        self.Label10.configure(foreground="#000000")
        self.Label10.configure(highlightbackground="#d9d9d9")
        self.Label10.configure(highlightcolor="black")

        self.Label10_1 = tk.Label(self.Frame4)
        self.Label10_1.place(relx=0.0, rely=0.066, height=2, width=393)
        self.Label10_1.configure(activebackground="#f9f9f9")
        self.Label10_1.configure(activeforeground="black")
        self.Label10_1.configure(anchor='w')
        self.Label10_1.configure(background="#2a2d34")
        self.Label10_1.configure(compound='left')
        self.Label10_1.configure(disabledforeground="#a3a3a3")
        self.Label10_1.configure(foreground="#000000")
        self.Label10_1.configure(highlightbackground="#d9d9d9")
        self.Label10_1.configure(highlightcolor="black")

        self.userHeight = 0.122
        for user in online:
            if len(user) > 0:
                self.Label14 = tk.Label(self.Frame4)
                self.Label14.place(relx=0.122, rely=self.userHeight, height=29, width=28)
                self.Label14.configure(activebackground="#f9f9f9")
                self.Label14.configure(activeforeground="black")
                self.Label14.configure(anchor='center')
                self.Label14.configure(background="#1f2023")
                self.Label14.configure(compound='left')
                self.Label14.configure(disabledforeground="#a3a3a3")
                self.Label14.configure(foreground="#ffffff")
                self.Label14.configure(highlightbackground="#d9d9d9")
                self.Label14.configure(highlightcolor="black")
                self.Label14.configure(font="-family {Segoe UI} -size 12 -weight bold")
                self.Label14.configure(text=user[0])

                self.Label8_1 = tk.Label(self.Frame4)
                self.Label8_1.place(relx=0.229, rely=self.userHeight, height=15, width=435)
                self.Label8_1.configure(activebackground="#f9f9f9")
                self.Label8_1.configure(activeforeground="black")
                self.Label8_1.configure(anchor='w')
                self.Label8_1.configure(background="#2f3035")
                self.Label8_1.configure(compound='left')
                self.Label8_1.configure(disabledforeground="#a3a3a3")
                self.Label8_1.configure(font="-family {Segoe UI} -size 10 -weight bold")
                self.Label8_1.configure(foreground="#ffffff")
                self.Label8_1.configure(highlightbackground="#d9d9d9")
                self.Label8_1.configure(highlightcolor="black")
                self.Label8_1.configure(text=user)
                self.userHeight += 0.05

        self.buttonHeight = 0.115
        for group in groups:
            if len(group) > 0:
                Button1_1 = tk.Button(self.Frame1)
                Button1_1.place(relx=0.192, rely=self.buttonHeight, height=46, width=46)
                Button1_1.configure(activebackground="#5865f2")
                Button1_1.configure(activeforeground="white")
                Button1_1.configure(activeforeground="#ffffff")
                Button1_1.configure(background="#36393f")
                Button1_1.configure(borderwidth="0")
                Button1_1.configure(compound='left')
                Button1_1.configure(disabledforeground="#a3a3a3")
                Button1_1.configure(foreground="#ffffff")
                Button1_1.configure(highlightbackground="#d9d9d9")
                Button1_1.configure(highlightcolor="black")
                Button1_1.configure(pady="0")
                Button1_1.configure(text=group)
                Button1_1.bind('<Button-1>', lambda event, g=group, b=Button1_1: self.getSubgroup(g, b))
                self.groupButtons.append(Button1_1)
                self.buttonHeight += 0.06

        self.menubar = tk.Menu(top,font="TkMenuFont",bg='#36393f',fg=_fgcolor)
        self.top.configure(menu = self.menubar)

    def addGroup(self, event):
        d = DiscordGroup.Toplevel1(self)

    def join(self, event):
        d = DiscordJoin.Toplevel1(self)

    def getSubgroup(self, group, button):
        for groupButton in self.groupButtons:
            groupButton.configure(background="#36393f")
        button.configure(background="#5865f2")
        self.group = group

        threading.Thread(target=self.sock.createMessage, args=("GET_SUBGROUPS", group, None)).start()

    def logout(self, event):
        threading.Thread(target=self.sock.createMessage, args=("SIGN_OUT", None, None)).start()

    def addOnline(self, name):
        self.online.append(name)
        self.Label14 = tk.Label(self.Frame4)
        self.Label14.place(relx=0.122, rely=self.userHeight, height=29, width=28)
        self.Label14.configure(activebackground="#f9f9f9")
        self.Label14.configure(activeforeground="black")
        self.Label14.configure(anchor='center')
        self.Label14.configure(background="#1f2023")
        self.Label14.configure(compound='left')
        self.Label14.configure(disabledforeground="#a3a3a3")
        self.Label14.configure(foreground="#ffffff")
        self.Label14.configure(highlightbackground="#d9d9d9")
        self.Label14.configure(highlightcolor="black")
        self.Label14.configure(font="-family {Segoe UI} -size 12 -weight bold")
        self.Label14.configure(text=name[0])

        self.Label8_1 = tk.Label(self.Frame4)
        self.Label8_1.place(relx=0.229, rely=self.userHeight, height=15, width=435)
        self.Label8_1.configure(activebackground="#f9f9f9")
        self.Label8_1.configure(activeforeground="black")
        self.Label8_1.configure(anchor='w')
        self.Label8_1.configure(background="#2f3035")
        self.Label8_1.configure(compound='left')
        self.Label8_1.configure(disabledforeground="#a3a3a3")
        self.Label8_1.configure(font="-family {Segoe UI} -size 10 -weight bold")
        self.Label8_1.configure(foreground="#ffffff")
        self.Label8_1.configure(highlightbackground="#d9d9d9")
        self.Label8_1.configure(highlightcolor="black")
        self.Label8_1.configure(text=name)
        self.userHeight += 0.05

    def removeOnline(self, name):
        self.online.remove(name)
        Frame6List = self.Frame6.winfo_children()
        Frame6List.append(self.Frame6)
        for widget in self.Frame4.winfo_children():
            if widget not in Frame6List:
                widget.destroy()
        self.userHeight = 0.122
        for user in self.online:
            if len(user) > 0:
                self.Label14 = tk.Label(self.Frame4)
                self.Label14.place(relx=0.122, rely=self.userHeight, height=29, width=28)
                self.Label14.configure(activebackground="#f9f9f9")
                self.Label14.configure(activeforeground="black")
                self.Label14.configure(anchor='center')
                self.Label14.configure(background="#1f2023")
                self.Label14.configure(compound='left')
                self.Label14.configure(disabledforeground="#a3a3a3")
                self.Label14.configure(foreground="#ffffff")
                self.Label14.configure(highlightbackground="#d9d9d9")
                self.Label14.configure(highlightcolor="black")
                self.Label14.configure(font="-family {Segoe UI} -size 12 -weight bold")
                self.Label14.configure(text=user[0])

                self.Label8_1 = tk.Label(self.Frame4)
                self.Label8_1.place(relx=0.229, rely=self.userHeight, height=15, width=435)
                self.Label8_1.configure(activebackground="#f9f9f9")
                self.Label8_1.configure(activeforeground="black")
                self.Label8_1.configure(anchor='w')
                self.Label8_1.configure(background="#2f3035")
                self.Label8_1.configure(compound='left')
                self.Label8_1.configure(disabledforeground="#a3a3a3")
                self.Label8_1.configure(font="-family {Segoe UI} -size 10 -weight bold")
                self.Label8_1.configure(foreground="#ffffff")
                self.Label8_1.configure(highlightbackground="#d9d9d9")
                self.Label8_1.configure(highlightcolor="black")
                self.Label8_1.configure(text=user)
                self.userHeight += 0.05

    def hideAll(self, event):
        if self.chat is not None:
            self.chat.destroy()
        if self.subgroups is not None:
            self.subgroups.destroy()

    def refresh(self):
        self.top.update_idletasks()
        self.top.update()


