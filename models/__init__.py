from .db import db
from .Types import TaskType, TaskStatus, ProxyType, AccountStatus, \
                    MemberStatus, Language, Gender, UserStatus
from .User import User, UserSettings
from .Member import Member
from .Chat import Chat
from .LogData import LogData
from .Account import Proxy, Account, ConnectionData
from .Message import Message
from .Task import Task
# Many to models
# user to
from .UserToTask import UserToTask
from .UserToChat import UserToChat
from .UserToMessage import UserToMessage
from .UserToAccounts import UserToAccounts
from .UserToGender import UserToGender
from .UserToStatus import UserToStatus, UserToSettings
# member to
from .MemberToChat import MemberToChat
from .MemberToTask import MemberToTask
# Log to
from .LogToTask import LogToTask
# accounts to
from .AccsToGroup import AccountToGroup, AccountGroup


def create_data_base():
    db.connect()
    db.create_tables([TaskType, TaskStatus, ProxyType, AccountStatus, MemberStatus, Language, Gender,
                      UserStatus, AccountGroup])
    db.create_tables([User, UserSettings, Member, Chat, LogData, Proxy, Account, ConnectionData, Message, Task])
    db.create_tables([UserToChat, UserToTask, UserToAccounts, UserToMessage, UserToStatus, UserToSettings, UserToGender])
    db.create_tables([MemberToChat, MemberToTask, LogToTask, AccountToGroup])
    db.close()

