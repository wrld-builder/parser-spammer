import os
import sys
from parse import Parse

def clear_screen():
    if sys.platform == 'linux' or 'linux2':
        os.system('clear')
    elif sys.platform == 'win32':
        os.system('cls')

def list_chats():
    parser = Parse()
    parser.get_all_user_chats()
    for index, chat in enumerate(parser.users_group):
        print(f'[{index}] ' + str(chat[1]))
    return parser
