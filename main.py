# This is a sample Python script
from enum import Enum
from datetime import datetime
from models import *
from user_class.User import MainUser

# Testing user Object

class message:
    from_user = User(id=175807698,
                     is_bot=False,
                     first_name='Igor',
                     last_name=None,
                     username='igor_d0',
                     language_code='ru',
                     is_premium=None,
                     added_to_attachment_menu=None,
                     can_join_groups=None,
                     can_read_all_group_messages=None,
                     supports_inline_queries=None)


if __name__ == '__main__':
    create_data_base()
    Test_User = MainUser(message.from_user, is_auto_create=True)
    print(Test_User.first_name, Test_User.last_name, Test_User.language_code)
    Test_User.connect("ofF")
