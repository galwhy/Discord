import tkinter as tk
import threading


class Toplevel1:
    def __init__(self, sock, frame, subgroupName, messages, top, username):
        self.frame = frame
        self.sock = sock
        self.subgroupName = subgroupName
        self.top = top
        self.username = username

        for widget in self.frame.winfo_children():
            widget.destroy()
        self.frame.pack_forget()

        self.Entry1 = tk.Entry(frame)
        self.Entry1.place(relx=0.03, rely=0.9, height=32, relwidth=0.941)
        self.Entry1.configure(background="#484b52")
        self.Entry1.configure(borderwidth="0")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#ffffff")
        self.Entry1.configure(highlightbackground="#d9d9d9")
        self.Entry1.configure(highlightcolor="black")
        self.Entry1.configure(insertbackground="#ffffff")
        self.Entry1.configure(selectbackground="blue")
        self.Entry1.configure(selectforeground="white")
        self.Entry1.bind('<Return>', self.send)

        self.Label5 = tk.Label(frame)
        self.Label5.place(relx=0.03, rely=0.87, height=4, width=886)
        self.Label5.configure(activebackground="#f9f9f9")
        self.Label5.configure(activeforeground="black")
        self.Label5.configure(anchor='w')
        self.Label5.configure(background="#3d4047")
        self.Label5.configure(compound='left')
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(foreground="#000000")
        self.Label5.configure(highlightbackground="#383b42")
        self.Label5.configure(highlightcolor="black")
        self.Label5.configure(highlightthickness="1")

        self.Text1 = tk.Text(frame)
        self.Text1.place(relx=0.066, rely=0.065, relheight=0.799, relwidth=0.86)
        self.Text1.configure(background="#363940")
        self.Text1.configure(borderwidth="0")
        self.Text1.configure(font="TkTextFont")
        self.Text1.configure(foreground="#ffffff")
        self.Text1.configure(highlightbackground="#d9d9d9")
        self.Text1.configure(highlightcolor="black")
        self.Text1.configure(insertbackground="black")
        self.Text1.configure(selectbackground="blue")
        self.Text1.configure(selectforeground="white")
        self.Text1.configure(font="-family {Segoe UI} -size 11")
        self.Text1.configure(wrap="word")
        self.Text1.insert("end", messages)
        self.Text1.configure(state='disabled')
        self.Text1.yview_pickplace("end")

        self.Label9 = tk.Label(frame)
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

        self.Label9_1 = tk.Label(frame)
        self.Label9_1.place(relx=0.0, rely=0.066, height=2, width=944)
        self.Label9_1.configure(activebackground="#f9f9f9")
        self.Label9_1.configure(activeforeground="black")
        self.Label9_1.configure(anchor='w')
        self.Label9_1.configure(background="#33363b")
        self.Label9_1.configure(borderwidth="0")
        self.Label9_1.configure(compound='left')
        self.Label9_1.configure(disabledforeground="#a3a3a3")
        self.Label9_1.configure(foreground="#000000")
        self.Label9_1.configure(highlightbackground="#33363b")
        self.Label9_1.configure(highlightcolor="#25262b")
        self.Label9_1.configure(padx="0")
        self.Label9_1.configure(pady="0")

        self.Label11 = tk.Label(frame)
        self.Label11.place(relx=0.05, rely=0.016, height=23, width=755)
        self.Label11.configure(activebackground="#f9f9f9")
        self.Label11.configure(activeforeground="black")
        self.Label11.configure(anchor='w')
        self.Label11.configure(background="#363940")
        self.Label11.configure(compound='left')
        self.Label11.configure(disabledforeground="#a3a3a3")
        self.Label11.configure(font="-family {Segoe UI} -size 12 -weight bold")
        self.Label11.configure(foreground="#ffffff")
        self.Label11.configure(highlightbackground="#d9d9d9")
        self.Label11.configure(highlightcolor="black")
        self.Label11.configure(text=self.subgroupName)

        self.Label12 = tk.Label(frame)
        self.Label12.place(relx=0.03, rely=0.016, height=23, width=21)
        self.Label12.configure(activebackground="#f9f9f9")
        self.Label12.configure(activeforeground="black")
        self.Label12.configure(anchor='w')
        self.Label12.configure(background="#363940")
        self.Label12.configure(compound='left')
        self.Label12.configure(disabledforeground="#a3a3a3")
        self.Label12.configure(font="-family {Segoe UI} -size 15 -weight bold")
        self.Label12.configure(foreground="#ffffff")
        self.Label12.configure(highlightbackground="#d9d9d9")
        self.Label12.configure(highlightcolor="black")
        self.Label12.configure(text='''#''')

    def send(self, event):
        message = self.Entry1.get()
        self.Entry1.delete(0, 'end')
        if message[0] == "\n": message = message[1:]

        threading.Thread(target=self.sock.createMessage, args=("SEND_MESSAGE", message, self.subgroupName)).start()
        message = f"{self.username} - {message}\n"

        self.Text1.config(state='normal')
        self.Text1.insert("end", message)
        self.Text1.config(state='disabled')
        self.Text1.see(tk.END)

    def destroy(self):
        for widget in self.frame.winfo_children():
            if widget != self.Label9 and widget != self.Label9_1:
                widget.destroy()
        self.frame.pack_forget()

    def refresh(self):
        self.top.update_idletasks()
        self.top.update()
