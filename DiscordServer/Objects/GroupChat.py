import sqlite3


class GroupChat:
    def __init__(self, connection):
        self.id = 0
        self.name = ""
        self.cursor = connection.cursor()
        self.insertCommand = f"INSERT INTO groupchat(Name) VALUES(?);"
        self.deleteCommand = "DELETE FROM groupchat WHERE id = ?"
        self.updateNameCommand = "UPDATE groupchat SET name = ? WHERE id = ?"
        self.selectIdCommand = "SELECT * FROM groupchat WHERE id = ?"
        self.selectNameCommand = "SELECT * FROM groupchat WHERE name = ?"

    def createNew(self,name):
        self.name = name
        args = (name, )
        self.cursor.execute(self.insertCommand, args)

    def deleteGroup(self, group_id):
        args = (group_id, )
        self.cursor.execute(self.deleteCommand, args)

    def updateName(self, group_id, name):
        args = (name, group_id)
        self.cursor.execute(self.updateNameCommand, args)

    def selectGroupId(self, group_id):
        args = (group_id, )
        self.cursor.execute(self.selectIdCommand, args)
        return self.cursor.fetchall()

    def selectGroupName(self, group_name):
        args = (group_name, )
        self.cursor.execute(self.selectNameCommand, args)
        return self.cursor.fetchall()