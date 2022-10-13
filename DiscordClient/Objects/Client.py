import socket
import threading
import queue


class client:
    def __init__(self, port, ip):
        self.port = port
        self.ip = ip
        self.address = (ip, port)
        self.sock = socket.socket()
        self.messageQueue = queue.Queue()

    def start(self):
        try:
            self.sock.connect(self.address)
            self.connected = True
            print("Conncted")
            thread = threading.Thread(target=self.receive)
            thread.start()
        except socket.error:
            print("Couldn't connect.")

    def receive(self):
        while True:
            message = ""
            while True:
                try:
                    data = self.sock.recv(4)
                except socket.error:
                    break
                if data != b'':
                    length = int(data.decode())
                    message += self.sock.recv(length).decode()
                    break
                else:
                    break

            messageList = message.split('~')
            if messageList[0] == "QUIT":
                self.sock.close()
                break
            #if messageList[0] == "NEW_MESSAGE" or messageList[0] == "MESSAGES" or messageList[0] == "NEW_USER" or messageList[0] == "DISCONNECT":
             #   self.messageQueue.put(messageList)
            if len(messageList) > 1:
                self.messageQueue.put(messageList)
            else:
                self.messageQueue.put(messageList[0])

    def sendToServer(self, message):
        if self.sock and not self.sock._closed:
            try:
                self.sock.sendall(message.encode())
            except socket.error:
                return

    def createMessage(self, request, str1, str2):
        message = f"{request}~{str1}~{str2}"
        messageLength = "0" * (4 - len(f"{len(message)}")) + f"{len(message)}"
        message = f"{messageLength}{message}"
        self.sendToServer(message)

    def disconnect(self):
        self.createMessage("QUIT", None, None)



