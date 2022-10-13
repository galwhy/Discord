import sqlite3


class Message:
    def __init__(self, connection):
        self.id = 0
        self.content = ""
        self.subgroup_id = 0
        self.cursor = connection.cursor()
        self.insertCommand = f"INSERT INTO message(content, subgroup_id, user_id) VALUES(?, ?, ?);"
        self.deleteMessageCommand = "DELETE FROM message WHERE id = ?"
        self.deleteSubgroupCommand = "DELETE FROM message WHERE subgroup_id = ?"
        self.updateCommand = "UPDATE message SET content = ? WHERE id = ?"
        self.selectMessageCommand = "SELECT * FROM message WHERE id = ?"
        self.selectSubgroupCommand = "SELECT * FROM message WHERE subgroup_id = ?"
        self.selectLastMessageCommand = "SELECT LAST_INSERT_ROWID() FROM message"

    def createNew(self, content, subgroup_id, user_id):
        self.content = content
        self.subgroup_id = subgroup_id
        args = (content, subgroup_id, user_id)
        self.cursor.execute(self.insertCommand, args)

    def deleteMessage(self, message_id):
        args = (message_id, )
        self.cursor.execute(self.deleteMessageCommand, args)

    def deleteSubgroup(self, subgroup_id):
        args = (subgroup_id, )
        self.cursor.execute(self.deleteSubgroupCommand, args)

    def updateMessage(self, message_id, content):
        args = (content, message_id)
        self.cursor.execute(self.updateCommand, args)

    def selectMessage(self, message_id):
        args = (message_id, )
        self.cursor.execute(self.selectMessageCommand, args)
        return self.cursor.fetchall()

    def selectSubgroup(self, subgroup_id):
        args = (subgroup_id, )
        self.cursor.execute(self.selectSubgroupCommand, args)
        return self.cursor.fetchall()

    def selectLastMessage(self):
        self.cursor.execute(self.selectLastMessageCommand)
        return self.cursor.fetchall()

