import tkinter as tk
from Gui import DiscordGroup
import threading


class Toplevel1:
    def __init__(self, mainScreen):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
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

        self.Frame7 = tk.Frame(self.frame)
        self.Frame7.place(relx=0.254, rely=0.215, relheight=0.5, relwidth=0.5)
        self.Frame7.configure(relief="groove")
        self.Frame7.configure(background="#ffffff")
        self.Frame7.configure(highlightbackground="#d9d9d9")
        self.Frame7.configure(highlightcolor="black")

        self.Label16 = tk.Label(self.Frame7)
        self.Label16.place(relx=0.0, rely=0.081, height=51, width=605)
        self.Label16.configure(activebackground="#f9f9f9")
        self.Label16.configure(activeforeground="black")
        self.Label16.configure(background="#ffffff")
        self.Label16.configure(compound='left')
        self.Label16.configure(disabledforeground="#a3a3a3")
        self.Label16.configure(font="-family {Segoe UI} -size 22 -weight bold")
        self.Label16.configure(foreground="#000000")
        self.Label16.configure(highlightbackground="#d9d9d9")
        self.Label16.configure(highlightcolor="black")
        self.Label16.configure(text='''customize your server''')

        self.Label17 = tk.Label(self.Frame7)
        self.Label17.place(relx=0.0, rely=0.201, height=51, width=605)
        self.Label17.configure(activebackground="#f9f9f9")
        self.Label17.configure(activeforeground="black")
        self.Label17.configure(background="#ffffff")
        self.Label17.configure(compound='left')
        self.Label17.configure(disabledforeground="#a3a3a3")
        self.Label17.configure(font="-family {Segoe UI} -size 10")
        self.Label17.configure(foreground="#777c84")
        self.Label17.configure(highlightbackground="#d9d9d9")
        self.Label17.configure(highlightcolor="black")
        self.Label17.configure(text='''Give your new server a personality with a name. You can always change it later.''')
        self.Label17.configure(wraplength="400")

        self.Label18 = tk.Label(self.Frame7)
        self.Label18.place(relx=0.051, rely=0.62, height=27, width=120)
        self.Label18.configure(activebackground="#4752c4")
        self.Label18.configure(activeforeground="white")
        self.Label18.configure(activeforeground="#ffffff")
        self.Label18.configure(anchor='w')
        self.Label18.configure(background="#ffffff")
        self.Label18.configure(compound='left')
        self.Label18.configure(disabledforeground="#a3a3a3")
        self.Label18.configure(font="-family {Segoe UI} -size 10 -weight bold")
        self.Label18.configure(foreground="#515862")
        self.Label18.configure(highlightbackground="#d9d9d9")
        self.Label18.configure(highlightcolor="black")
        self.Label18.configure(text='''Server name''')

        self.Entry3 = tk.Entry(self.Frame7)
        self.Entry3.place(relx=0.051, rely=0.683, height=41, relwidth=0.899)
        self.Entry3.configure(background="#e3e5e8")
        self.Entry3.configure(borderwidth="0")
        self.Entry3.configure(disabledforeground="#a3a3a3")
        self.Entry3.configure(font="TkFixedFont")
        self.Entry3.configure(foreground="#000000")
        self.Entry3.configure(highlightbackground="#d9d9d9")
        self.Entry3.configure(highlightcolor="black")
        self.Entry3.configure(insertbackground="black")
        self.Entry3.configure(selectbackground="blue")
        self.Entry3.configure(selectforeground="white")

        self.Frame8 = tk.Frame(self.Frame7)
        self.Frame8.place(relx=0.0, rely=0.821, relheight=0.189, relwidth=1.0)
        self.Frame8.configure(relief="groove")
        self.Frame8.configure(background="#f2f3f5")
        self.Frame8.configure(highlightbackground="#d9d9d9")
        self.Frame8.configure(highlightcolor="black")

        self.Button4 = tk.Button(self.Frame8)
        self.Button4.place(relx=0.802, rely=0.302, height=44, width=90)
        self.Button4.configure(activebackground="#4752c4")
        self.Button4.configure(activeforeground="white")
        self.Button4.configure(activeforeground="#ffffff")
        self.Button4.configure(background="#5865f2")
        self.Button4.configure(borderwidth="0")
        self.Button4.configure(compound='left')
        self.Button4.configure(disabledforeground="#a3a3a3")
        self.Button4.configure(font="-family {Segoe UI} -size 10 -weight bold")
        self.Button4.configure(foreground="#ffffff")
        self.Button4.configure(highlightbackground="#d9d9d9")
        self.Button4.configure(highlightcolor="black")
        self.Button4.configure(pady="0")
        self.Button4.configure(text='''Create''')
        self.Button4.bind('<Button-1>', self.create)

        self.Button5 = tk.Button(self.Frame8)
        self.Button5.place(relx=0.051, rely=0.302, height=44, width=47)
        self.Button5.configure(activebackground="#ececec")
        self.Button5.configure(activeforeground="#000000")
        self.Button5.configure(background="#f2f3f5")
        self.Button5.configure(borderwidth="0")
        self.Button5.configure(compound='left')
        self.Button5.configure(disabledforeground="#a3a3a3")
        self.Button5.configure(font="-family {Segoe UI} -size 11 -weight bold")
        self.Button5.configure(foreground="#434444")
        self.Button5.configure(highlightbackground="#d9d9d9")
        self.Button5.configure(highlightcolor="black")
        self.Button5.configure(pady="0")
        self.Button5.configure(text='''Back''')
        self.Button5.bind('<Button-1>', self.back)

        self.Button6 = tk.Button(self.Frame7)
        self.Button6.place(relx=0.919, rely=0.03, height=28, width=27)
        self.Button6.configure(activebackground="#ececec")
        self.Button6.configure(activeforeground="#000000")
        self.Button6.configure(background="#ffffff")
        self.Button6.configure(borderwidth="0")
        self.Button6.configure(compound='left')
        self.Button6.configure(disabledforeground="#a3a3a3")
        self.Button6.configure(foreground="#000000")
        self.Button6.configure(highlightbackground="#d9d9d9")
        self.Button6.configure(highlightcolor="black")
        photo_location = "Images/exit.png"
        global _img2
        _img2 = tk.PhotoImage(file=photo_location)
        self.Button6.configure(image=_img2)
        self.Button6.configure(pady="0")
        self.Button6.bind('<Button-1>', self.exit)

    def exit(self, event):
        self.Frame7.destroy()

    def back(self, event):
        self.Frame7.destroy()
        d = DiscordGroup.Toplevel1(self.mainScreen)

    def create(self, event):
        groupName = self.Entry3.get()

        threading.Thread(target=self.sock.createMessage, args=("CREATE_GROUP", groupName, None)).start()
        while self.sock.messageQueue.empty():
            self.refresh()
        clientMessage = self.sock.messageQueue.get()

        self.Entry3.delete(0, 'end')

        if clientMessage == "GTIT":
            self.createGroupButton(groupName)
            self.Frame7.destroy()
        elif clientMessage == "GROUP_EXIST":
            self.Button4.configure(text='''Group Exists''', background="red")
            self.top.after(1000, lambda: self.Button4.configure(text='''Create''', background="#5865f2"))

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


