import sqlite3


class GroupsMemberships:
    def __init__(self, connection):
        self.user_id = 0
        self.group_id = 0
        self.cursor = connection.cursor()
        self.insertCommand = f"INSERT INTO groupsmemberships(user_id, group_id) VALUES(?, ?);"
        self.deleteUserCommand = "DELETE FROM groupsmemberships WHERE user_id = ?"
        self.deleteGroupCommand = "DELETE FROM groupsmemberships WHERE group_id = ?"
        self.selectUserCommand = "SELECT * FROM groupsmemberships WHERE user_id = ?"
        self.selectGroupCommand = "SELECT * FROM groupsmemberships WHERE group_id = ?"
        self.selectGroupUserCommand = "SELECT * FROM groupsmemberships WHERE group_id = ? and user_id = ?"


    def createNew(self, user_id, group_id):
        self.user_id = user_id
        self.group_id = group_id
        args = (user_id, group_id)
        self.cursor.execute(self.insertCommand, args)

    def deleteUser(self, user_id):
        args = (user_id, )
        self.cursor.execute(self.deleteUserCommand, args)

    def deleteGroup(self, group_id):
        args = (group_id, )
        self.cursor.execute(self.deleteGroupCommand, args)

    def selectUser(self, user_id):
        args = (user_id, )
        self.cursor.execute(self.selectUserCommand, args)
        return self.cursor.fetchall()

    def selectGroup(self, group_id):
        args = (group_id, )
        self.cursor.execute(self.selectGroupCommand, args)
        return self.cursor.fetchall()

    def selectGroupUser(self, group_id, user_id):
        args = (group_id, user_id)
        self.cursor.execute(self.selectGroupUserCommand, args)
        return self.cursor.fetchall()