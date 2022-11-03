from datetime import datetime
from models.User import User
from models import db, Chat
from models.Message import Message
from models.Account import Account, ConnectionData,Proxy
from models.UserToAccounts import UserToAccounts
from models.UserToMessage import UserToMessage
from models.Types import ProxyType
from models.AccsToGroup import AccountGroup, AccountToGroup
from models.UserToChat import UserToChat


class UserError(Exception):
    def __init__(self, m):
        self.message = m

    def __str__(self):
        return self.message


def connect_database():
    db.connect()


def close_database():
    db.close()


class MainUser:
    id = None
    first_name = None
    last_name = None
    username = None
    language_code = None
    user_id = int
    created_at = None

    # On class initialisation , searching for user inside database
    # If user not found , create new user / or skip
    # After
    def __init__(self, _user_data: any, is_auto_create: bool):
        def create_user(_user_data: _user_data):
            print("creating new user")
            new_user = User.create(
                first_name=_user_data.first_name,
                last_name=_user_data.last_name,
                username=_user_data.username,
                language_code=_user_data.language_code,
                user_id=_user_data.id
            )

            if new_user.id is not None:
                self.id = new_user.id
                self.first_name = new_user.first_name
                self.last_name = new_user.first_name
                self.user_id = new_user.user_id
                self.language_code = new_user.language_code
                self.username = new_user.username
                self.created_at = new_user.created_at

        def check_user(_user_data: _user_data):
            db.connect()
            # if message.text == "/start"
            try:
                query = User.select().where(User.user_id == _user_data.id).get()
                self.id = query.id
                self.first_name = query.first_name
                self.last_name = query.last_name
                self.username = query.username
                self.language_code = query.language_code
                self.created_at = query.created_at
            except Exception as ex:
                print(f"Error: {ex}")
                if is_auto_create:
                    create_user(_user_data)

        check_user(_user_data)

    # Set new message to db
    def add_msg(self, msg):
        new_message = Message.create(
            content=msg.content,
        )
        UserToMessage.create(
            message_id=new_message.id,
            user_id=self.user_id
        )
        return new_message

    # ____new for test___
    # getting all messages by user from db
    def get_list_msg(self):
        messages = UserToMessage.select().where(UserToMessage.user_id == self.user_id).get()
        data = {}
        for msg in messages:
            data += Message.select().where(Message.id == msg.id)
        return data

    def remove_msg(self, msg):
        try:
            Message.delete().where(Message.id == msg.id).execute()
            print(f"Deleted msg: {msg.id}")
        except Exception as ex:
            raise UserError(f'Delete nat available: {ex}')

    def edit_msg(self, msg, text):
        try:
            Message.update(content=text, created_at=datetime.now()).where(Message.id == msg.id).execute()
            print(f"Updated msg: {msg.id}")
        except Exception as ex:
            raise UserError(f"Update not available: {ex}")

    def add_account(self, account):
        check_acc = Account.select().where(Account.phone == account.phone).get()
        if check_acc is None:
            new_account = Account.create(
                is_valid=True,
                phone=account.phone,
                status_id=1
            )
            UserToAccounts.create(
                user_id=self.user_id,
                account_id=new_account.id
            )
            return True

        raise UserError(f"Error with account {account.phone}")

    def get_list_accounts(self):
        accounts = UserToAccounts.select().where(UserToAccounts.user_id == self.user_id).get()
        data = {}
        for acc_id in accounts:
            data += Account.select().where(Account.id == acc_id.id).get()
        return data

    def get_curr_account(self,account_id):
        return Account.select().where(Account.id == account_id).get()

    def add_account_connect(self, api_id, api_hash,account_id):
        check = ConnectionData.select().where(ConnectionData.api_id == api_id).get()
        if check is None:
            new_connection = ConnectionData.create(
                api_id=api_id,
                api_hash=api_hash
            )
            Account.update(connect_id=new_connection.id).where(Account.id == account_id).execute()

            return True

        raise UserError(f"Connection not added")

    def edit_account_connect(self, connect_id, api_id, api_hash):
        try:
            ConnectionData.update(
                api_id=api_id,
                api_hash=api_hash
            ).where(ConnectionData.id == connect_id).execute()
        except Exception as ex:
            raise UserError(f"Update not available: {ex}")

    def remove_connect(self, connect_id, account_id):
        try:
            ConnectionData.delete().where(ConnectionData.id == connect_id).execute()
            Account.update(
                connect_id=None
            ).where(Account.id == account_id).execute()

        except Exception as ex:
            raise UserError(f"Delete not available: {ex}")

    def get_connect(self, account_id):
        try:
            account = Account.select().where(Account.id == account_id).get()
            return  ConnectionData.select().where(ConnectionData.id == account.connect_id).get()
        except Exception as ex:
            raise UserError(f"Connection error: {ex}")

    def connect_list(self):
        account_list = UserToAccounts.select().where(UserToAccounts.user_id == self.user_id).get()
        account_lst = {}
        for acc_id in account_list:
            account_lst += acc_id

        connection_list = {}
        account_list = {}

        for acc_id in account_lst:
            account_list += Account.select().where(Account.id == acc_id.id).get()

        for prox in account_list:
            connection_list += ConnectionData.select().where(ConnectionData.id == prox.connection_id).get()

        return connection_list

    def add_proxy(self, proxy):
        proxy_type = ProxyType.select().where(ProxyType.title == proxy.type).get()
        new_proxy = Proxy.create(
            type_id=proxy_type.id,
            address=proxy.address,
            password=proxy.password,
            login=proxy.login,
            is_valid=True
        )
        return new_proxy

    def add_proxy_to_account(self,account_id, proxy_id):
        try:
            Account.update(proxy_id=proxy_id).where(Account.id == account_id).execute()
        except Exception as ex:
            raise UserError(f"Proxy not added to account: {ex}")

    def edit_proxy(self, proxy_id, proxy):
        try:
            Proxy.update(
                type_id=1,
                address=proxy.address,
                password=proxy.password,
                login=proxy.login,
                is_valid=True
            ).where(Proxy.id == proxy_id).execute()
        except Exception as ex:
            raise UserError(f"Error proxy: {ex}")

    def remove_proxy(self, proxy_id, account_id):
        try:
            Proxy.delete().where(Proxy.id == proxy_id).execute()
            Account.update(
                proxy_id=None
            ).where(Account.id == account_id, Account.proxy_id == proxy_id).execute()
        except Exception as ex:
            raise UserError(f"Proxy not deleted: {ex}")

    def get_proxy(self, account_id):
        try:
            proxy_id = Account.select().where(Account.id == account_id).get()
            return Proxy.select().where(Proxy.id == proxy_id.proxy_id).get()
        except Exception as ex:
            raise UserError(f"Proxy error: {ex}")

    def get_proxy_list(self):
        account_list = UserToAccounts.select().where(UserToAccounts.user_id == self.user_id).get()
        account_lst = {}
        for acc_id in account_list:
            account_lst += acc_id

        proxy_list = {}
        account_list = {}

        for acc_id in account_lst:
            account_list += Account.select().where(Account.id == acc_id.id).get()

        for prox in account_list:
            proxy_list += Proxy.select().where(Proxy.id == prox.proxy_id).get()

        return proxy_list

    def add_group(self, title):
        new_group = AccountGroup.create(
            title=title,
            group_owner=self.user_id
        )
        return new_group

    def edit_group_title(self, title, group_id):
        updated_group = AccountGroup.update(
            title=title
        ).where(AccountGroup.id == group_id).execute()

        return updated_group

    def get_group_list(self):
        return AccountGroup.select().where(AccountGroup.group_owner == self.user_id).get()

    def add_acc_to_group(self, account_id, group_id):
        AccountToGroup.create(
            account_id=account_id,
            group_id=group_id
        )

    def remove_acc_from_group(self, account_id, group_id):
        AccountToGroup.delete().where(AccountToGroup.account_id == account_id,
                                      AccountToGroup.group_id == group_id).execute()

    def add_update_chat(self, chat):
        is_exist = Chat.select().where(Chat.chat_id == chat.id).get()
        if is_exist is None:
            new_chat = Chat.create(
                url=chat.url,
                count_users=chat.count_users,
                title=chat.title,
                chat_id=chat.id
            )
            UserToChat.create(
                chat_id=new_chat.chat_id,
                user_id=self.user_id
            )
            return "Chat added"
        else:
            Chat.update(
                url=chat.url,
                count_users=chat.count_users,
                title=chat.title
            ).where(Chat.chat_id == chat.chat_id).execute()
            return "Updated"

    def get_chat_list(self):
        chats_ids = UserToChat.select().where(UserToChat.user_id == self.user_id).get()
        chats_back = {}

        for chat_id in chats_ids:
            chats_back += Chat.select().where(Chat.chat_id == chat_id.chat_id).get()

        return chats_back

    def remove_chat(self, chat_id):
        try:
            Chat.delete().where(Chat.chat_id == chat_id).execute()
            UserToChat.delete().where(UserToChat.chat_id == chat_id, UserToChat.user_id == self.user_id).get()
        except Exception as ex:
            raise UserError(f"Remove error: {ex}")





    # Method allows you to connect/disconnect SQLite3 database
    # Use str for identify commands: On/Off
    def connect(self, command: str):
        if command.lower() == "on":
            connect_database()
        elif command.lower() == "off":
            close_database()
        else:
            raise UserError(f"Command not available: {command}")
