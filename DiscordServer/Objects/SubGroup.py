import sqlite3


class SubGroup:
    def __init__(self, connection):
        self.id = 0
        self.name = ""
        self.group_id = 0
        self.cursor = connection.cursor()
        self.insertCommand = f"INSERT INTO subgroup(Name, group_id) VALUES(?, ?);"
        self.deleteSubgroupCommand = "DELETE FROM subgroup WHERE id = ?"
        self.deleteGroupCommand = "DELETE FROM subgroup WHERE group_id = ?"
        self.updateNameCommand = "UPDATE subgroup SET name = ? WHERE id = ?"
        self.selectSubgroupCommand = "SELECT * FROM subgroup WHERE id = ?"
        self.selectGroupCommand = "SELECT * FROM subgroup WHERE group_id = ?"
        self.selectNameCommand = "SELECT * FROM subgroup WHERE name = ?"


    def createNew(self,name, group_id):
        self.name = name
        self.group_id = group_id
        args = (name, group_id)
        self.cursor.execute(self.insertCommand, args)

    def deleteSubgroup(self, subgroup_id):
        args = (subgroup_id, )
        self.cursor.execute(self.deleteSubgroupCommand, args)

    def deleteGroup(self, group_id):
        args = (group_id, )
        self.cursor.execute(self.deleteGroupCommand, args)

    def updateName(self, subgroup_id, name):
        args = (name, subgroup_id)
        self.cursor.execute(self.updateNameCommand, args)

    def selectSubgroup(self, subgroup_id):
        args = (subgroup_id, )
        self.cursor.execute(self.selectSubgroupCommand, args)
        return self.cursor.fetchall()

    def selectGroup(self, group_id):
        args = (group_id, )
        self.cursor.execute(self.selectGroupCommand, args)
        return self.cursor.fetchall()

    def selectSubgroupName(self, subgroupName):
        args = (subgroupName, )
        self.cursor.execute(self.selectNameCommand, args)
        return self.cursor.fetchall()
