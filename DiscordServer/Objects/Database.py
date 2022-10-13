from Objects import User
from Objects import GroupChat
from Objects import GroupsMemberships
from Objects import Message
from Objects import NewMessages
from Objects import SubGroup

class Database:
    def __init__(self, connection):
        self.users = User.User(connection)
        self.groupChats = GroupChat.GroupChat(connection)
        self.groupsMemberships = GroupsMemberships.GroupsMemberships(connection)
        self.messages = Message.Message(connection)
        self.newMessages = NewMessages.NewMessages(connection)
        self.subGroups = SubGroup.SubGroup(connection)
        self.connection = connection