import tkinter as tk
import threading
from Gui import DiscordMain


class Toplevel1:

    def __init__(self, sock, top):
        self.Login = True

        self.sock = sock
        self.username = ""

        self.top = top
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9'  # X11 color: 'gray85'
        _ana1color = '#d9d9d9'  # X11 color: 'gray85'
        _ana2color = '#ececec'  # Closest X11 color: 'gray92'
        self.top.geometry("1920x1017+46+176")
        self.top.minsize(120, 1)
        self.top.maxsize(1924, 1061)
        self.top.resizable(1, 1)
        self.top.title("Toplevel 0")
        self.top.configure(background="#d9d9d9")
        self.top.configure(highlightbackground="#d9d9d9")
        self.top.configure(highlightcolor="black")

        self.Label1 = tk.Label(self.top)
        self.Label1.place(relx=0.0, rely=0.0, height=1017, width=1920)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(anchor='w')
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(borderwidth="0")
        self.Label1.configure(compound='left')
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        photo_location = "Images/discord.png"
        global _img0
        _img0 = tk.PhotoImage(file=photo_location)
        self.Label1.configure(image=_img0)

        self.Frame1 = tk.Frame(self.top)
        self.Frame1.place(relx=0.325, rely=0.325, relheight=0.342, relwidth=0.35)
        self.Frame1.configure(relief='raised')
        self.Frame1.configure(borderwidth="1")
        self.Frame1.configure(relief="raised")
        self.Frame1.configure(background="#36393f")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="black")
        self.Frame1.configure(padx="10")
        self.Frame1.configure(pady="10")
        self.Frame1.configure(takefocus="10")

        self.Label1 = tk.Label(self.Frame1)
        self.Label1.place(relx=0.0, rely=0.0, height=67, width=471)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#36393f")
        self.Label1.configure(borderwidth="0")
        self.Label1.configure(compound='center')
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font="-family {Segoe UI} -size 16")
        self.Label1.configure(foreground="#fcfcfc")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="#ffffff")
        self.Label1.configure(padx="0")
        self.Label1.configure(pady="0")
        self.Label1.configure(text='''Welcome back!''')

        self.Entry1 = tk.Entry(self.Frame1)
        self.Entry1.place(relx=0.101, rely=0.351, height=35, relwidth=0.5)
        self.Entry1.configure(background="#303339")
        self.Entry1.configure(borderwidth="0")
        self.Entry1.configure(disabledbackground="#7289da")
        self.Entry1.configure(disabledforeground="#e2e3e7")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#ffffff")
        self.Entry1.configure(highlightbackground="#222428")
        self.Entry1.configure(highlightcolor="#7289da")
        self.Entry1.configure(highlightthickness="1")
        self.Entry1.configure(insertbackground="#ffffff")
        self.Entry1.configure(readonlybackground="#7289da")
        self.Entry1.configure(relief="solid")
        self.Entry1.configure(selectbackground="#7289da")
        self.Entry1.configure(selectforeground="#7289da")

        self.Entry1_1 = tk.Entry(self.Frame1)
        self.Entry1_1.place(relx=0.101, rely=0.601, height=35, relwidth=0.5)
        self.Entry1_1.configure(background="#303339")
        self.Entry1_1.configure(borderwidth="0")
        self.Entry1_1.configure(disabledbackground="#000000")
        self.Entry1_1.configure(disabledforeground="#a3a3a3")
        self.Entry1_1.configure(font="TkFixedFont")
        self.Entry1_1.configure(foreground="#ffffff")
        self.Entry1_1.configure(highlightbackground="#222428")
        self.Entry1_1.configure(highlightcolor="#7289da")
        self.Entry1_1.configure(highlightthickness="1")
        self.Entry1_1.configure(insertbackground="#ffffff")
        self.Entry1_1.configure(readonlybackground="#4c4c4c")
        self.Entry1_1.configure(relief="solid")
        self.Entry1_1.configure(selectbackground="#000000")
        self.Entry1_1.configure(selectforeground="#4c4c4c")

        self.Label2 = tk.Label(self.Frame1)
        self.Label2.place(relx=0.104, rely=0.287, height=18, width=128)
        self.Label2.configure(activebackground="#4a4a4a")
        self.Label2.configure(activeforeground="white")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(anchor='w')
        self.Label2.configure(background="#36393f")
        self.Label2.configure(compound='left')
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font="-family {Segoe UI} -size 10")
        self.Label2.configure(foreground="#8e9297")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''Username''')

        self.Label3 = tk.Label(self.Frame1)
        self.Label3.place(relx=0.104, rely=0.546, height=17, width=128)
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(activeforeground="black")
        self.Label3.configure(anchor='w')
        self.Label3.configure(background="#36393f")
        self.Label3.configure(compound='left')
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(font="-family {Segoe UI} -size 10")
        self.Label3.configure(foreground="#8e9297")
        self.Label3.configure(highlightbackground="#d9d9d9")
        self.Label3.configure(highlightcolor="black")
        self.Label3.configure(text='''Password''')

        self.Button1 = tk.Button(self.Frame1)
        self.Button1.place(relx=0.101, rely=0.81, height=34, width=336)
        self.Button1.configure(activebackground="#4752c4")
        self.Button1.configure(activeforeground="white")
        self.Button1.configure(activeforeground="#ffffff")
        self.Button1.configure(background="#7288da")
        self.Button1.configure(borderwidth="0")
        self.Button1.configure(compound='left')
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#ffffff")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Login''')
        self.Button1.bind('<Button-1>', self.login)

        self.Frame2 = tk.Frame(self.Frame1)
        self.Frame2.place(relx=0.661, rely=0.098, relheight=0.802, relwidth = 0.004)
        self.Frame2.configure(relief="groove")
        self.Frame2.configure(background="#42454a")
        self.Frame2.configure(highlightbackground="#d9d9d9")
        self.Frame2.configure(highlightcolor="black")

        self.Label4 = tk.Label(self.Frame1)
        self.Label4.place(relx=0.147, rely=0.149, height=35, width=295)
        self.Label4.configure(activebackground="#42454a")
        self.Label4.configure(activeforeground="white")
        self.Label4.configure(activeforeground="#42454a")
        self.Label4.configure(background="#36393f")
        self.Label4.configure(compound='left')
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(font="-family {Segoe UI} -size 12")
        self.Label4.configure(foreground="#686c72")
        self.Label4.configure(highlightbackground="#d9d9d9")
        self.Label4.configure(highlightcolor="black")
        self.Label4.configure(text='''We're so excited to see you again!''')

        self.Button2 = tk.Button(self.Frame1)
        self.Button2.place(relx=0.251, rely=0.92, height=24, width=47)
        self.Button2.configure(activebackground="#36393f")
        self.Button2.configure(activeforeground="white")
        self.Button2.configure(activeforeground="#ffffff")
        self.Button2.configure(background="#36393f")
        self.Button2.configure(borderwidth="0")
        self.Button2.configure(compound='left')
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#7289da")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''Register''')
        self.Button2.bind('<Button-1>', self.handleSignup)

        self.Label5 = tk.Label(self.Frame1)
        self.Label5.place(relx=0.1, rely=0.92, height=24, width=98)
        self.Label5.configure(anchor='w')
        self.Label5.configure(background="#36393f")
        self.Label5.configure(compound='left')
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(foreground="#62666c")
        self.Label5.configure(text='''Need an account?''')

    def login(self, event):
        self.username = self.Entry1.get()
        password = self.Entry1_1.get()

        threading.Thread(target=self.sock.createMessage, args=("SIGN_IN", self.username, password)).start()
        while self.sock.messageQueue.empty():
            self.refresh()
        clientMessage = self.sock.messageQueue.get()

        self.Entry1.delete(0, 'end')
        self.Entry1_1.delete(0, 'end')

        if clientMessage == "GTIT":
            self.top.quit()
        elif clientMessage == "WRONG_USER":
            self.Button1.configure(text='''Wrong password/username''', background="red")
            self.top.after(1000, lambda : self.Button1.configure(text='''Login''', background="#7288da"))
        elif clientMessage == "USER_CONNECTED":
            self.Button1.configure(text='''User Already Connected''', background="red")
            self.top.after(1000, lambda: self.Button1.configure(text='''Login''', background="#7288da"))

    def signup(self, event):
        self.username = self.Entry1.get()
        password = self.Entry1_1.get()

        threading.Thread(target=self.sock.createMessage, args=("SIGN_UP", self.username, password)).start()
        while self.sock.messageQueue.empty():
            self.refresh()
        clientMessage = self.sock.messageQueue.get()

        self.Entry1.delete(0, 'end')
        self.Entry1_1.delete(0, 'end')

        if clientMessage == "GTIT":
            self.top.quit()
        elif clientMessage == "USER_EXIST":
            self.Button1.configure(text='''User Exists''', background="red")
            self.top.after(1000, lambda: self.Button1.configure(text='''Register''', background="#7288da"))

    def handleSignup(self, event):
        if self.Login:
            self.Button1.configure(text='''Register''')
            self.Button1.bind('<Button-1>', self.signup)
            self.Button2.configure(text='''Login''')
            self.Login = False
        elif not self.Login:
            self.Button1.configure(text='''Login''')
            self.Button2.configure(text='''Register''')
            self.Button1.bind('<Button-1>', self.login)
            self.Login = True

    def refresh(self):
        self.top.update_idletasks()
        self.top.update()

