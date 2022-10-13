import threading
import tkinter
from Objects import Client
from Gui import DiscordLogin
from Gui import DiscordMain
from Gui import DiscordChat
from Gui import DiscordSubgroups
import tkinter as tk
a = False


def createMessage(request, str1, str2, client):
    message = f"{request}~{str1}~{str2}"
    messageLength = "0" * (4 - len(f"{len(message)}")) + f"{len(message)}"
    message = f"{messageLength}{message}"
    client.sendToServer(message)
    while client.messageQueue.empty():
        continue
    clientMessage = client.messageQueue.get()
    return clientMessage


def refresh(top):
    if not a:
        top.update_idletasks()
        top.update()
    else:
        exit()


def onClose(top, client):
    global a
    a = True
    top.destroy()
    client.disconnect()


def main():
    ip = input("Enter server ip address: ")
    port = 6900
    client = Client.client(port, ip)
    client.start()

    top = tkinter.Tk()
    top.protocol("WM_DELETE_WINDOW", lambda t=top, c=client: onClose(t, c))

    while not a:
        loginScreen = DiscordLogin.Toplevel1(client, top)
        loginScreen.top.mainloop()
        threading.Thread(target=client.createMessage, args=("GET_GROUPS", None, None)).start()
        while client.messageQueue.empty():
            refresh(top)
        clientMessage = client.messageQueue.get()
        groups = []
        if isinstance(clientMessage, list):
            groups = clientMessage[1:]

        threading.Thread(target=client.createMessage, args=("GET_ONLINE", None, None)).start()
        while client.messageQueue.empty():
            refresh(top)
        clientMessage = client.messageQueue.get()
        online = []
        if isinstance(clientMessage, list):
            online = clientMessage[1:]

        mainScreen = DiscordMain.Toplevel1(client, top, groups, loginScreen.username, online)
        while not a:
            while client.messageQueue.empty():
                refresh(top)
            clientMessage = client.messageQueue.get()
            if clientMessage[0] == "NEW_USER":
                mainScreen.addOnline(clientMessage[1])
            elif clientMessage[0] == "DISCONNECT":
                mainScreen.removeOnline(clientMessage[1])
            elif clientMessage[0] == "MESSAGES" or clientMessage == "MESSAGES":
                messages = ""
                clientMessage = clientMessage[1:]
                if isinstance(clientMessage, list):
                    for i in range(0, len(clientMessage), 2):
                        if clientMessage[i] != "":
                            messages += f"{clientMessage[i]} - {clientMessage[i + 1]}\n"

                d = DiscordChat.Toplevel1(client, mainScreen.Frame3, mainScreen.subgroup, messages, top, mainScreen.username)
                mainScreen.chat = d
            elif len(mainScreen.Frame3.winfo_children()) > 2 and clientMessage[0] == "NEW_MESSAGE":
                if clientMessage[3] == mainScreen.subgroup:
                    clientMessage = clientMessage[1:]
                    messages = f"{clientMessage[0]} - {clientMessage[1]}\n"
                    d.Text1.config(state='normal')
                    d.Text1.insert("end", messages)
                    d.Text1.config(state='disabled')
                    d.Text1.see(tk.END)
            elif clientMessage[0] == "IN_SUBGROUPS":
                subgroups = clientMessage[1:]
                subgroups = DiscordSubgroups.Toplevel1(mainScreen, subgroups, mainScreen.group)
            elif clientMessage == "OUT":
                break


if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
