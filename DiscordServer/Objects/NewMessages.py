import sqlite3


class NewMessages:
    def __init__(self, connection):
        self.user_id = 0
        self.message_id = 0
        self.cursor = connection.cursor()
        self.insertCommand = f"INSERT INTO newmessages(user_id, message_id) VALUES(?, ?);"
        self.deleteUserCommand = "DELETE FROM newmessages WHERE user_id = ?"
        self.deleteMessageCommand = "DELETE FROM newmessages WHERE message_id = ?"
        self.selectUserCommand = "SELECT * FROM newmessages WHERE user_id = ?"
        self.selectMessageCommand = "SELECT * FROM newmessages WHERE message_id = ?"
        self.deleteCommand = "DELETE FROM newmessages WHERE message_id = ? and user_id = ?"


    def createNew(self, user_id, message_id):
        self.user_id = user_id
        self.message_id = message_id
        args = (user_id, message_id)
        self.cursor.execute(self.insertCommand, args)

    def deleteUser(self, user_id):
        args = (user_id, )
        self.cursor.execute(self.deleteUserCommand, args)

    def deleteMessage(self, message_id):
        args = (message_id, )
        self.cursor.execute(self.deleteMessageCommand, args)

    def selectUser(self, user_id):
        args = (user_id, )
        self.cursor.execute(self.selectUserCommand, args)
        return self.cursor.fetchall()

    def selectMessage(self, message_id):
        args = (message_id, )
        self.cursor.execute(self.selectMessageCommand, args)
        return self.cursor.fetchall()

    def delete(self, messageId, userId):
        args = (messageId, userId)
        self.cursor.execute(self.deleteCommand, args)