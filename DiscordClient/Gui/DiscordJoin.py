import tkinter as tk
import threading
from Gui import DiscordGroup


class Toplevel1:
    def __init__(self, mainScreen):
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        self.mainScreen = mainScreen
        self.top = mainScreen.top
        self.sock = mainScreen.sock
        self.frame = mainScreen.Frame3
        self.groupFrame = mainScreen.Frame1
        self.buttonHeight = mainScreen.buttonHeight

        self.Frame9 = tk.Frame(self.frame)
        self.Frame9.place(relx=0.3, rely=0.25, relheight=0.5, relwidth=0.4)
        self.Frame9.configure(relief="groove")
        self.Frame9.configure(background="#ffffff")

        self.Label20 = tk.Label(self.Frame9)
        self.Label20.place(relx=0.0, rely=0.049, height=36, width=484)
        self.Label20.configure(background="#ffffff")
        self.Label20.configure(borderwidth="0")
        self.Label20.configure(compound='left')
        self.Label20.configure(disabledforeground="#a3a3a3")
        self.Label20.configure(font="-family {Segoe UI} -size 19 -weight bold")
        self.Label20.configure(foreground="#000000")
        self.Label20.configure(text='''Join a Server''')

        self.Label16 = tk.Label(self.Frame9)
        self.Label16.place(relx=0.0, rely=0.12, height=36, width=484)
        self.Label16.configure(background="#ffffff")
        self.Label16.configure(borderwidth="0")
        self.Label16.configure(compound='left')
        self.Label16.configure(disabledforeground="#a3a3a3")
        self.Label16.configure(font="-family {Segoe UI} -size 11")
        self.Label16.configure(foreground="#979ba1")
        self.Label16.configure(text='''Enter a name below to join an existing server.''')

        self.Label17 = tk.Label(self.Frame9)
        self.Label17.place(relx=0.05, rely=0.255, height=23, width=41)
        self.Label17.configure(anchor='w')
        self.Label17.configure(background="#ffffff")
        self.Label17.configure(compound='left')
        self.Label17.configure(disabledforeground="#a3a3a3")
        self.Label17.configure(font="-family {Segoe UI} -size 10")
        self.Label17.configure(foreground="#5d636c")
        self.Label17.configure(text='''Name''')

        self.Entry4 = tk.Entry(self.Frame9)
        self.Entry4.place(relx=0.05, rely=0.314, height=30, relwidth=0.89)
        self.Entry4.configure(background="#e3e5e8")
        self.Entry4.configure(borderwidth="0")
        self.Entry4.configure(disabledforeground="#a3a3a3")
        self.Entry4.configure(font="TkFixedFont")
        self.Entry4.configure(foreground="#000000")
        self.Entry4.configure(insertbackground="black")

        self.Frame7 = tk.Frame(self.Frame9)
        self.Frame7.place(relx=0.0, rely=0.87, relheight=0.13, relwidth=1.0)
        self.Frame7.configure(relief="groove")
        self.Frame7.configure(background="#f2f3f5")

        self.Button6 = tk.Button(self.Frame7)
        self.Button6.place(relx=0.75, rely=0.258, height=36, width=97)
        self.Button6.configure(activebackground="#4752c4")
        self.Button6.configure(activeforeground="white")
        self.Button6.configure(activeforeground="#ffffff")
        self.Button6.configure(background="#5865f2")
        self.Button6.configure(borderwidth="0")
        self.Button6.configure(compound='left')
        self.Button6.configure(disabledforeground="#a3a3a3")
        self.Button6.configure(font="-family {Segoe UI} -size 10 -weight bold")
        self.Button6.configure(foreground="#ffffff")
        self.Button6.configure(highlightbackground="#d9d9d9")
        self.Button6.configure(highlightcolor="black")
        self.Button6.configure(pady="0")
        self.Button6.configure(relief="sunken")
        self.Button6.configure(text='''Join server''')
        self.Button6.bind('<Button-1>', self.join)

        self.Button7 = tk.Button(self.Frame7)
        self.Button7.place(relx=0.083, rely=0.258, height=36, width=47)
        self.Button7.configure(activebackground="#f2f3f5")
        self.Button7.configure(activeforeground="#000000")
        self.Button7.configure(background="#f2f3f5")
        self.Button7.configure(borderwidth="0")
        self.Button7.configure(compound='left')
        self.Button7.configure(disabledforeground="#a3a3a3")
        self.Button7.configure(font="-family {Segoe UI} -size 10 -weight bold")
        self.Button7.configure(foreground="#000000")
        self.Button7.configure(highlightbackground="#d9d9d9")
        self.Button7.configure(highlightcolor="black")
        self.Button7.configure(pady="0")
        self.Button7.configure(text='''Back''')
        self.Button7.bind('<Button-1>', self.back)

        self.Button8 = tk.Button(self.Frame9)
        self.Button8.place(relx=0.919, rely=0.02, height=28, width=28)
        self.Button8.configure(activebackground="#ffffff")
        self.Button8.configure(activeforeground="#000000")
        self.Button8.configure(background="#ffffff")
        self.Button8.configure(borderwidth="0")
        self.Button8.configure(compound='left')
        self.Button8.configure(disabledforeground="#a3a3a3")
        self.Button8.configure(foreground="#000000")
        self.Button8.configure(highlightbackground="#d9d9d9")
        self.Button8.configure(highlightcolor="black")
        photo_location = "Images/exit.png"
        global _img2
        _img2 = tk.PhotoImage(file=photo_location)
        self.Button8.configure(image=_img2)
        self.Button8.configure(pady="0")
        self.Button8.bind('<Button-1>', self.exit)

    def exit(self, event):
        self.Frame9.destroy()

    def back(self, event):
        self.Frame9.destroy()
        d = DiscordGroup.Toplevel1(self.mainScreen)

    def join(self, event):
        groupName = self.Entry4.get()

        threading.Thread(target=self.sock.createMessage, args=("JOIN_GROUP", groupName, None)).start()
        while self.sock.messageQueue.empty():
            self.refresh()
        clientMessage = self.sock.messageQueue.get()

        self.Entry4.delete(0, 'end')

        if clientMessage == "GTIT":
            self.createGroupButton(groupName)
            self.Frame9.destroy()
        elif clientMessage == "GROUP_NO_EXIST":
            self.Button6.configure(text='''Wrong Group''', background="red")
            self.top.after(1000, lambda: self.Button6.configure(text='''Create''', background="#5865f2"))
        elif clientMessage == "MEMBERSHIP_EXIST":
            self.Button6.configure(text='''In Group''', background="red")
            self.top.after(1000, lambda: self.Button6.configure(text='''Create''', background="#5865f2"))

    def createGroupButton(self, name):
        Button1_1 = tk.Button(self.groupFrame)
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
        Button1_1.configure(text=name)
        Button1_1.bind('<Button-1>', lambda event, g=name, b=Button1_1: self.mainScreen.getSubgroup(g, b))
        self.mainScreen.groupButtons.append(Button1_1)
        self.mainScreen.buttonHeight += 0.06

    def refresh(self):
        self.top.update_idletasks()
        self.top.update()

