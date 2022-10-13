import sqlite3


class User:
    def __init__(self, connection):
        self.user_id = 0
        self.name = ""
        self.password = ""
        self.cursor = connection.cursor()
        self.insertCommand = "INSERT INTO User(Name, PassWord) VALUES(?, ?);"
        self.deleteCommand = "DELETE FROM user WHERE id = ?"
        self.updatePasswordCommand = "UPDATE user SET password = ? WHERE id = ?"
        self.updateNameCommand = "UPDATE user SET name = ? WHERE id = ?"
        self.selectCommand = "SELECT * FROM user WHERE id = ?"
        self.selectNamePasswordCommand = "SELECT * FROM user WHERE name = ? and password = ?"
        self.selectNameCommand = "SELECT * FROM user WHERE name = ?"

    def createNew(self,name, password):
        self.name = name
        self.password = password
        args = (name, password)
        self.cursor.execute(self.insertCommand, args)

    def deleteUser(self, user_id):
        args = (user_id, )
        self.cursor.execute(self.deleteCommand, args)

    def updatePassword(self, user_id, password):
        args = (password, user_id)
        self.cursor.execute(self.updatePasswordCommand, args)

    def updateName(self, user_id, name):
        args = (name, user_id)
        self.cursor.execute(self.updateNameCommand, args)

    def selectUser(self, user_id):
        args = (user_id, )
        self.cursor.execute(self.selectCommand, args)
        return self.cursor.fetchall()

    def selectNamePassword(self, name, password):
        args = (name, password)
        self.cursor.execute(self.selectNamePasswordCommand, args)
        return self.cursor.fetchall()

    def selectName(self, name):
        args = (name, )
        self.cursor.execute(self.selectNameCommand, args)
        return self.cursor.fetchall()


