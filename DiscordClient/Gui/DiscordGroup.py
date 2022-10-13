import tkinter as tk
from Gui import DiscordCustomize
from Gui import DiscordJoin


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

        self.Frame7 = tk.Frame(self.frame)
        self.Frame7.place(relx=0.275, rely=0.151, relheight=0.7
                , relwidth=0.445)
        self.Frame7.configure(relief="groove")
        self.Frame7.configure(background="#ffffff")
        self.Frame7.configure(highlightbackground="#d9d9d9")
        self.Frame7.configure(highlightcolor="black")

        self.Button4 = tk.Button(self.Frame7)
        self.Button4.place(relx=0.9, rely=0.018, height=35, width=35)
        self.Button4.configure(activebackground="#ffffff")
        self.Button4.configure(activeforeground="#000000")
        self.Button4.configure(background="#ffffff")
        self.Button4.configure(borderwidth="0")
        self.Button4.configure(compound='left')
        self.Button4.configure(disabledforeground="#a3a3a3")
        self.Button4.configure(foreground="#000000")
        self.Button4.configure(highlightbackground="#d9d9d9")
        self.Button4.configure(highlightcolor="black")
        photo_location = "Images/exit.png"
        global _img2
        _img2 = tk.PhotoImage(file=photo_location)
        self.Button4.configure(image=_img2)
        self.Button4.configure(pady="0")
        self.Button4.bind('<Button-1>', self.exit)

        self.Label16 = tk.Label(self.Frame7)
        self.Label16.place(relx=0.25, rely=0.039, height=37, width=269)
        self.Label16.configure(activebackground="#f9f9f9")
        self.Label16.configure(activeforeground="black")
        self.Label16.configure(background="#ffffff")
        self.Label16.configure(compound='left')
        self.Label16.configure(disabledforeground="#a3a3a3")
        self.Label16.configure(font="-family {Segoe UI} -size 20 -weight bold")
        self.Label16.configure(foreground="#000000")
        self.Label16.configure(highlightbackground="#d9d9d9")
        self.Label16.configure(highlightcolor="black")
        self.Label16.configure(text='''Create a server''')

        self.Label17 = tk.Label(self.Frame7)
        self.Label17.place(relx=0.0, rely=0.098, height=72, width=539)
        self.Label17.configure(activebackground="#f9f9f9")
        self.Label17.configure(activeforeground="black")
        self.Label17.configure(background="#ffffff")
        self.Label17.configure(compound='left')
        self.Label17.configure(disabledforeground="#a3a3a3")
        self.Label17.configure(font="-family {Segoe UI} -size 10")
        self.Label17.configure(foreground="#777c84")
        self.Label17.configure(highlightbackground="#d9d9d9")
        self.Label17.configure(highlightcolor="black")
        self.Label17.configure(text='''Tour server is where you and your friends hang out. Make yours and start talking.''')
        self.Label17.configure(wraplength="350")

        self.Button5 = tk.Button(self.Frame7)
        self.Button5.place(relx=0.098, rely=0.902, height=42, width=432)
        self.Button5.configure(activebackground="#4f5660")
        self.Button5.configure(activeforeground="white")
        self.Button5.configure(activeforeground="#ffffff")
        self.Button5.configure(background="#6a7480")
        self.Button5.configure(borderwidth="0")
        self.Button5.configure(compound='left')
        self.Button5.configure(disabledforeground="#a3a3a3")
        self.Button5.configure(font="-family {Segoe UI} -size 10 -weight bold")
        self.Button5.configure(foreground="#ffffff")
        self.Button5.configure(highlightbackground="#d9d9d9")
        self.Button5.configure(highlightcolor="black")
        self.Button5.configure(pady="0")
        self.Button5.configure(text='''Join a Server''')
        self.Button5.bind('<Button-1>', self.join)

        self.Button6 = tk.Button(self.Frame7)
        self.Button6.place(relx=0.048, rely=0.25, height=72, width=486)
        self.Button6.configure(activebackground="#e7e9eb")
        self.Button6.configure(activeforeground="#000000")
        self.Button6.configure(anchor='w')
        self.Button6.configure(background="#ffffff")
        self.Button6.configure(borderwidth="1")
        self.Button6.configure(compound='left')
        self.Button6.configure(disabledforeground="#a3a3a3")
        self.Button6.configure(font="-family {Segoe UI} -size 12 -weight bold")
        self.Button6.configure(foreground="#000000")
        self.Button6.configure(highlightbackground="#c9cdd2")
        self.Button6.configure(highlightcolor="#c9cdd2")
        self.Button6.configure(highlightthickness="0")
        self.Button6.configure(overrelief="solid")
        self.Button6.configure(padx="20")
        self.Button6.configure(pady="0")
        self.Button6.configure(relief="solid")
        self.Button6.configure(text='''Create My Own''')
        self.Button6.bind('<Button-1>', self.createNew)

        self.Label18 = tk.Label(self.Frame7)
        self.Label18.place(relx=0.85, rely=0.26, height=57, width=23)
        self.Label18.configure(activebackground="#f9f9f9")
        self.Label18.configure(activeforeground="black")
        self.Label18.configure(background="#ffffff")
        self.Label18.configure(compound='left')
        self.Label18.configure(disabledforeground="#a3a3a3")
        self.Label18.configure(font="-family {Segoe UI} -size 15 -weight bold")
        self.Label18.configure(foreground="#000000")
        self.Label18.configure(highlightbackground="#d9d9d9")
        self.Label18.configure(highlightcolor="black")
        self.Label18.configure(text='''>''')

        self.Label19 = tk.Label(self.Frame7)
        self.Label19.place(relx=0.0, rely=0.85, height=27, width=539)
        self.Label19.configure(activebackground="#f9f9f9")
        self.Label19.configure(activeforeground="black")
        self.Label19.configure(background="#ffffff")
        self.Label19.configure(compound='left')
        self.Label19.configure(disabledforeground="#a3a3a3")
        self.Label19.configure(font="-family {Segoe UI} -size 11 -weight bold")
        self.Label19.configure(foreground="#000000")
        self.Label19.configure(highlightbackground="#d9d9d9")
        self.Label19.configure(highlightcolor="black")
        self.Label19.configure(text='''Have an invite already?''')

    def exit(self, event):
        self.Frame7.destroy()

    def createNew(self, event):
        self.Frame7.destroy()
        d = DiscordCustomize.Toplevel1(self.mainScreen)

    def join(self, event):
        self.Frame7.destroy()
        d = DiscordJoin.Toplevel1(self.mainScreen)

