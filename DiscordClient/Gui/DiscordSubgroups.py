import tkinter as tk
import threading
from Gui import DiscordNewSubgroup
from Gui import DiscordChat


class Toplevel1:
    def __init__(self, mainScreen, subgroups, groupName):
        self.sock = mainScreen.sock
        self.frame = mainScreen.Frame2
        self.mainScreen = mainScreen
        self.groupName = groupName
        self.top = mainScreen.top

        userDataFrame = mainScreen.Frame5.winfo_children()
        userDataFrame.append(mainScreen.Frame5)

        mainScreen.subgroupButtons = []
        for widget in self.frame.winfo_children():
            if widget not in userDataFrame:
                widget.destroy()
        self.frame.pack_forget()

        self.Label3 = tk.Label(self.frame)
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

        self.Label4 = tk.Label(self.frame)
        self.Label4.place(relx=0.05, rely=0.02, height=21, width=240)
        self.Label4.configure(activebackground="#f9f9f9")
        self.Label4.configure(activeforeground="black")
        self.Label4.configure(anchor='w')
        self.Label4.configure(background="#2f3035")
        self.Label4.configure(compound='left')
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(font="-family {Segoe UI} -size 12 -weight bold")
        self.Label4.configure(foreground="#ffffff")
        self.Label4.configure(highlightbackground="#d9d9d9")
        self.Label4.configure(highlightcolor="black")
        self.Label4.configure(text=groupName)

        self.Label3_1 = tk.Label(self.frame)
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

        self.Label15 = tk.Label(self.frame)
        self.Label15.place(relx=0.017, rely=0.085, height=22, width=124)
        self.Label15.configure(activebackground="#2f3035")
        self.Label15.configure(activeforeground="white")
        self.Label15.configure(anchor='w')
        self.Label15.configure(background="#2f3035")
        self.Label15.configure(compound='left')
        self.Label15.configure(disabledforeground="#a3a3a3")
        self.Label15.configure(font="-family {Segoe UI} -size 10 -weight bold")
        self.Label15.configure(foreground="#6d6e73")
        self.Label15.configure(text='''TEXT CHANNELS''')

        self.Button3 = tk.Button(self.frame)
        self.Button3.place(relx=0.8, rely=0.08, height=24, width=27)
        self.Button3.configure(activebackground="#2f3035")
        self.Button3.configure(activeforeground="white")
        self.Button3.configure(activeforeground="#ffffff")
        self.Button3.configure(background="#2f3035")
        self.Button3.configure(borderwidth="0")
        self.Button3.configure(compound='left')
        self.Button3.configure(disabledforeground="#a3a3a3")
        self.Button3.configure(font="-family {Segoe UI} -size 15 -weight bold")
        self.Button3.configure(foreground="#6d6e73")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(pady="0")
        self.Button3.configure(text='''+''')
        self.Button3.bind('<Button-1>', self.addSubgroup)

        self.subgroupHeight = 0.12
        for subgroup in subgroups:
            if len(subgroup) > 0:
                Label6 = tk.Label(self.frame)
                Label6.place(relx=0.021, rely=self.subgroupHeight, height=24, width=19)
                Label6.configure(activebackground="#f9f9f9")
                Label6.configure(activeforeground="black")
                Label6.configure(background="#2f3035")
                Label6.configure(compound='left')
                Label6.configure(disabledforeground="#a3a3a3")
                Label6.configure(font="-family {Segoe UI} -size 20")
                Label6.configure(foreground="#6d6e73")
                Label6.configure(highlightbackground="#d9d9d9")
                Label6.configure(highlightcolor="black")
                Label6.configure(text='''#''')

                Button2 = tk.Button(self.frame)
                Button2.place(relx=0.1, rely=self.subgroupHeight, height=24, width=192)
                Button2.configure(activebackground="#42454e")
                Button2.configure(activeforeground="white")
                Button2.configure(activeforeground="#ffffff")
                Button2.configure(anchor='w')
                Button2.configure(background="#2f3035")
                Button2.configure(borderwidth="0")
                Button2.configure(compound='left')
                Button2.configure(disabledforeground="#a3a3a3")
                Button2.configure(font="-family {Segoe UI} -size 10 -weight bold")
                Button2.configure(foreground="#6d6e73")
                Button2.configure(highlightbackground="#d9d9d9")
                Button2.configure(highlightcolor="black")
                Button2.configure(pady="0")
                Button2.configure(text=subgroup)
                Button2.bind('<Button-1>', lambda event, g=subgroup, b=Button2: self.getMessages(g, b))
                self.mainScreen.subgroupButtons.append(Button2)
                self.subgroupHeight += 0.04

    def getMessages(self, subgroup, button):
        self.mainScreen.subgroup = subgroup
        for subgroupButton in self.mainScreen.subgroupButtons:
            subgroupButton.configure(background="#2f3035")
        button.configure(background="#42454e")

        threading.Thread(target=self.sock.createMessage, args=("GET_MESSAGES", subgroup, None)).start()

    def addSubgroup(self, event):
        d = DiscordNewSubgroup.Toplevel1(self.mainScreen, self)

    def destroy(self):
        userDataFrame = self.mainScreen.Frame5.winfo_children()
        userDataFrame.append(self.mainScreen.Frame5)

        for widget in self.mainScreen.Frame2.winfo_children():
            if widget not in userDataFrame and widget != self.Label3_1:
                widget.destroy()
        self.mainScreen.Frame2.pack_forget()

    def refresh(self):
        self.top.update_idletasks()
        self.top.update()

