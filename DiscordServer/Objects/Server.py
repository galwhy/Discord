import socket
import _thread
import sqlite3
from Objects import Database



class Server:
    def __init__(self, port):
        self.clients = {}
        self.port = port
        print(f"Server IP: {socket.gethostbyname_ex(socket.gethostname())[2][0]}")
        Ip = socket.gethostbyname_ex(socket.gethostname())[2][0]
        self.address = (Ip, port)
        self.sock = socket.socket()
        self.sock.bind(self.address)

    def start(self):
        self.sock.listen(10)

        while True:
            (c, addr) = self.sock.accept()
            self.clients[c] = -1
            _thread.start_new_thread(self.createDatabase, (c,))

    def createDatabase(self, client):
        connection = sqlite3.connect("database/discordDatabase.sqlite")
        database = Database.Database(connection)
        self.rec_send(client, database)
        database.connection.close()

    def rec_send(self, client: socket.socket, database):
        while True:
            try:
                message = ""
                while True:
                    data = client.recv(4)
                    if data != b'':
                        length = int(data.decode())
                        message += client.recv(length).decode()
                        break
                    else:
                        break
                decipheredMessage = self.decipherMessage(message, client, database)
                if decipheredMessage is None or decipheredMessage[0] == "QUIT":

                    decipheredMessage = "QUIT"
                    messageLength = "0" * (4 - len(f"{len(decipheredMessage)}")) + f"{len(decipheredMessage)}"
                    decipheredMessage = f"{messageLength}{decipheredMessage}"
                    client.sendall(decipheredMessage.encode())
                    userId = self.clients[client]
                    self.clients.pop(client)
                    if userId != -1:
                        name = database.users.selectUser(userId)[0][1]
                        decipheredMessage = f"DISCONNECT~{name}"
                        messageLength = "0" * (4 - len(f"{len(decipheredMessage)}")) + f"{len(decipheredMessage)}"
                        decipheredMessage = f"{messageLength}{decipheredMessage}"
                        for c in self.clients:
                            if c != client:
                                c.sendall(decipheredMessage.encode())
                    break
                elif decipheredMessage[0] == "NEW_USER":
                    decipheredMessage = f"NEW_USER~{decipheredMessage[1]}"
                    messageLength = "0" * (4 - len(f"{len(decipheredMessage)}")) + f"{len(decipheredMessage)}"
                    decipheredMessage = f"{messageLength}{decipheredMessage}"
                    for c in self.clients:
                            if c != client and self.clients[c] != -1:
                                c.sendall(decipheredMessage.encode())
                    client.sendall("0004GTIT".encode())
                elif decipheredMessage[0] == "NEW_MESSAGE":
                    membershipList = decipheredMessage[2]
                    decipheredMessage = decipheredMessage[1]
                    messageLength = "0" * (4 - len(f"{len(decipheredMessage)}")) + f"{len(decipheredMessage)}"
                    decipheredMessage = f"{messageLength}{decipheredMessage}"
                    userIds = list(self.clients.values())
                    for membership in membershipList:
                        if membership[0] in userIds:
                            c = list(self.clients.keys())[list(self.clients.values()).index(membership[0])]
                            if c != client:
                                c.sendall(decipheredMessage.encode())
                elif decipheredMessage[0] == "DISCONNECT":
                    decipheredMessage = f"DISCONNECT~{decipheredMessage[1]}"
                    messageLength = "0" * (4 - len(f"{len(decipheredMessage)}")) + f"{len(decipheredMessage)}"
                    decipheredMessage = f"{messageLength}{decipheredMessage}"
                    for c in self.clients:
                        if c != client:
                            c.sendall(decipheredMessage.encode())
                    client.sendall("0003OUT".encode())
                else:
                    messageLength = "0" * (4 - len(f"{len(decipheredMessage)}")) + f"{len(decipheredMessage)}"
                    decipheredMessage = f"{messageLength}{decipheredMessage}"
                    client.sendall(decipheredMessage.encode())
            except socket.error:
                name = database.users.selectUser(self.clients[client])[0][1]
                self.clients.pop(client)
                decipheredMessage = f"DISCONNECT~{name}"
                messageLength = "0" * (4 - len(f"{len(decipheredMessage)}")) + f"{len(decipheredMessage)}"
                decipheredMessage = f"{messageLength}{decipheredMessage}"
                for c in self.clients:
                    if c != client:
                        c.sendall(decipheredMessage.encode())
                break

    def decipherMessage(self, message, client, database):
        messageList = message.split("~")
        if messageList[0] == "SIGN_IN":
            returnMessage = self.signIn(messageList[1], messageList[2], database)
            self.clients[client] = returnMessage[1]
            if returnMessage[0] == "NEW_USER":
                return returnMessage[0], messageList[1]
            else:
                return returnMessage[0]
        elif messageList[0] == "SIGN_UP":
            returnMessage = self.signUp(messageList[1], messageList[2], database)
            self.clients[client] = returnMessage[1]
            if returnMessage[0] == "NEW_USER":
                return returnMessage[0], messageList[1]
            else:
                return returnMessage[0]
        elif messageList[0] == "SIGN_OUT":
            name = database.users.selectUser(self.clients[client])[0][1]
            self.clients[client] = -1
            return "DISCONNECT", name
        elif messageList[0] == "CREATE_GROUP":
            returnMessage = self.createGroup(messageList[1], self.clients[client], database)
            return returnMessage
        elif messageList[0] == "JOIN_GROUP":
            returnMessage = self.joinGroup(messageList[1], self.clients[client], database)
            return returnMessage
        elif messageList[0] == "ADD_SUBGROUP":
            returnMessage = self.addSubgroup(messageList[1], messageList[2], database)
            return returnMessage
        elif messageList[0] == "UPDATE_ACCOUNT":
            returnMessage = self.updateAccount(messageList[1], messageList[2], self.clients[client], database)
            return returnMessage
        elif messageList[0] == "UPDATE_GROUP":
            returnMessage = self.updateGroup(messageList[1], messageList[2], database)
            return returnMessage
        elif messageList[0] == "UPDATE_SUBGROUP":
            returnMessage = self.updateSubgroup(messageList[1], messageList[2], database)
            return returnMessage
        elif messageList[0] == "GET_GROUPS":
            returnMessage = self.getGroups(self.clients[client], database)
            return returnMessage
        elif messageList[0] == "GET_SUBGROUPS":
            returnMessage = self.getSubgroups(messageList[1], database)
            return returnMessage
        elif messageList[0] == "GET_MESSAGES":
            returnMessage = self.getMessages(messageList[1], database)
            return returnMessage
        elif messageList[0] == "GET_NEW_MESSAGES_SUBGROUP":
            returnMessage = self.getNewMessageSubgroup(self.clients[client], database)
            return returnMessage
        elif messageList[0] == "GET_NEW_MESSAGES":
            returnMessage = self.getNewMessages(self.clients[client], messageList[1], database)
            return returnMessage
        elif messageList[0] == "SEND_MESSAGE":
            returnMessage = self.sendMessage(messageList[1], messageList[2], self.clients[client], database)
            return returnMessage
        elif messageList[0] == "GET_ONLINE":
            returnMessage = self.getOnline(database)
            return returnMessage
        elif messageList[0] == "GET_ONLINE_GROUP":
            returnMessage = self.getOnlineGroup(messageList[1], database)
            return returnMessage
        elif messageList[0] == "QUIT":
            return "QUIT"

    def signIn(self, username, password, database):
        usersList = database.users.selectNamePassword(username, password)
        if len(usersList) > 0:
            if usersList[0][0] in self.clients.values():
                return "USER_CONNECTED", -1
            return "NEW_USER", usersList[0][0]
        return "WRONG_USER", -1

    def signUp(self, username, password, database):
        usersList = database.users.selectName(username)
        if len(usersList) > 0:
            return "USER_EXIST", -1
        database.users.createNew(username, password)
        database.connection.commit()
        usersList = database.users.selectNamePassword(username, password)
        return "NEW_USER", usersList[0][0]

    def createGroup(self, groupName, userId, database):
        groupList = database.groupChats.selectGroupName(groupName)
        if len(groupList) > 0:
            return "GROUP_EXIST"
        database.groupChats.createNew(groupName)
        groupId = database.groupChats.selectGroupName(groupName)[0][0]
        database.groupsMemberships.createNew(userId, groupId)
        database.connection.commit()
        return "GTIT"

    def joinGroup(self, groupName, userId, database):
        groupList = database.groupChats.selectGroupName(groupName)
        if len(groupList) > 0:
            membershipsList = database.groupsMemberships.selectGroupUser(groupList[0][0], userId)
            if len(membershipsList) > 0:
                return "MEMBERSHIP_EXIST"
            database.groupsMemberships.createNew(userId, groupList[0][0])
            database.connection.commit()
            return "GTIT"
        return "GROUP_NO_EXIST"

    def addSubgroup(self, groupName, subgroupName, database):
        groupList = database.groupChats.selectGroupName(groupName)
        if len(groupList) > 0:
            subgroupList = database.subGroups.selectSubgroupName(subgroupName)
            if len(subgroupList) > 0:
                return "SUBGROUP_EXIST"
            database.subGroups.createNew(subgroupName, groupList[0][0])
            database.connection.commit()
            return "GTIT"
        return "GROUP_NO_EXIST"

    def updateAccount(self, newName, newPassword, userId, database):
        database.users.updateName(userId, newName)
        database.users.updatePassword(userId, newPassword)
        database.connection.commit()
        return "GTIT"

    def updateGroup(self, newName, groupName, database):
        groupList = database.groupChats.selectGroupName(groupName)
        if len(groupList) > 0:
            database.groupChats.updateName(groupList[0][0], newName)
            database.connection.commit()
            return "GTIT"
        return "GROUP_NO_EXIST"

    def updateSubgroup(self, newName, subgroupName, database):
        subgroupList = database.subGroups.selectSubgroupName(subgroupName)
        if len(subgroupList) > 0:
            database.subGroups.updateName(subgroupList[0][0], newName)
            database.connection.commit()
            return "GTIT"
        return "SUBGROUP_NO_EXIST"

    def getGroups(self, userId, database):
        groupMembershipList = database.groupsMemberships.selectUser(userId)
        groupsNames = ""
        for groupMembership in groupMembershipList:
            groupName = database.groupChats.selectGroupId(groupMembership[1])[0][1]
            groupsNames += f"~{groupName}"
        return "IN_GROUPS" + groupsNames

    def getSubgroups(self, groupName, database):
        groupList = database.groupChats.selectGroupName(groupName)
        if len(groupList) > 0:
            subgroupNames = ""
            subGroupList = database.subGroups.selectGroup(groupList[0][0])
            for subgroup in subGroupList:
                subgroupNames += f"~{subgroup[1]}"
            if len(subgroupNames) < 1:
                return "IN_SUBGROUPS~"
            return "IN_SUBGROUPS" + subgroupNames
        return "GROUP_NO_EXIST"

    def getNewMessageSubgroup(self, userId, database):
        newMessagesList = database.newMessages.selectUser(userId)
        if len(newMessagesList) > 0:
            subgroupNames = ""
            for message in newMessagesList:
                subgroupId = database.messages.selectMessage(message[1])[0][2]
                subgroupNames += f"~{database.subGroups.selectSubgroup(subgroupId)[0][1]}"
                return "NEW_MESSAGES_SUBGROUP"+subgroupNames
        return "NO_NEW_MESSAGES"

    def getNewMessages(self, userId, subgroupName, database):
        subgroupList = database.subGroups.selectSubgroupName(subgroupName)
        if len(subgroupList) > 0:
            subgroupId = subgroupList[0][0]
            newMessagesList = database.newMessages.selectUser(userId)
            if len(newMessagesList) > 0:
                Messages = ""
                for newMessage in newMessagesList:
                    messageId = newMessage[1]
                    message = database.messages.selectMessage(messageId)
                    if message[0][2] == subgroupId:
                        userName = database.users.selectUser(message[0][3])[0][1]
                        Messages += f"~{userName}~{message[0][1]}"
                        database.newMessages.delete(messageId, userId)
                database.connection.commit()
                return "NEW_MESSAGES"+Messages
            return "NO_NEW_MESSAGES"
        return "GROUP_NO_EXIST"

    def getMessages(self, subgroupName, database):
        subgroupList = database.subGroups.selectSubgroupName(subgroupName)
        if len(subgroupList) > 0:
            Messages = ""
            messageList = database.messages.selectSubgroup(subgroupList[0][0])
            for message in messageList:
                userId = message[3]
                userName = database.users.selectUser(userId)[0][1]
                Messages += f"~{userName}~{message[1]}"
            return "MESSAGES" + Messages
        return "SUBGROUP_NO_EXIST"

    def sendMessage(self, message, subgroupName, userId, database):
        subgroupList = database.subGroups.selectSubgroupName(subgroupName)
        if len(subgroupList) > 0:
            database.messages.createNew(message, subgroupList[0][0], userId)
            messageId = database.messages.selectLastMessage()[0][0]
            groupId = subgroupList[0][2]
            groupMembershipList = database.groupsMemberships.selectGroup(groupId)
            for groupMembership in groupMembershipList:
                if groupMembership[0] != userId:
                    database.newMessages.createNew(groupMembership[0], messageId)
            database.connection.commit()
            username = database.users.selectUser(userId)[0][1]
            return "NEW_MESSAGE", f"NEW_MESSAGE~{username}~{message}~{subgroupName}", groupMembershipList
        return "SUBGROUP_NO_EXIST"

    def getOnline(self, database):
        online = ""
        for client in self.clients:
            if self.clients[client] != -1:
                name = database.users.selectUser(self.clients[client])[0][1]
                online += f"~{name}"
        return "ONLINE"+online

    def getOnlineGroup(self, groupName, database):
        groupList = database.groupChats.selectGroupName(groupName)
        if len(groupList) > 0:
            online = ""
            for client in self.clients:
                membership = database.newMessages.selectUser(self.clients[client])
                if len(membership) > 0:
                    name = database.users.selectUser(self.clients[client])[0][1]
                    online += f"~{name}"
            return "ONLINE_GROUP"+online


