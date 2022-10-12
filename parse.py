from config import app
from pyrogram.enums import ChatType

class Parse:
    def __init__(self):
        self.users_group = []

    def get_all_user_chats(self):
        for dialog in app.get_dialogs():
            if dialog.chat.type == ChatType.GROUP:
                self.users_group.append([dialog.chat.id, dialog.chat.title])

    def del_useless_lines(self):
        unique_lines = set(open('dist/data.txt', 'r', encoding='utf-8').readlines())
        open('dist/data.txt', 'w', encoding='utf-8').writelines(set(unique_lines))

    def get_all_chat_members(self, current_chat_id):
        for member in app.get_chat_members(current_chat_id):
            print(member.user.first_name)
            if not(member.user.is_deleted or member.user.is_bot):
                with open('dist/data.txt', mode='a', encoding='utf-8') as file:
                    file.write(str(member.user.id) + ' ' + member.user.username + '\n')
        self.del_useless_lines()

    @property
    def user_group(self):
        return self.users_group
