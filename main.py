from config import app
import helper
import receiver
from spam import Spam
from adder import add_members_in_chat

if __name__ == '__main__':
    with app:
        method = 0
        while method != 4:
            method = int(input('[1] Parse users in chat\n[2] Spam to users\n[3] Add in chat\n[4] Exit\n>>> '))
            data_vector = receiver.Receiver().recognize_data('dist/data.txt')   # load database

            if method == 1:
                parser = helper.list_chats()
                current_chat_id = int(input('Enter the chat_id\n>>> '))
                parser.get_all_chat_members(parser.users_group[current_chat_id][0]) ; input('Press any key...')
            elif method == 2:
                message_to_spam = str(input('Enter your message to spam:\n>>> '))

                spammer = Spam()
                spammer.set_text_to_spam(message_to_spam)
                spammer.spam_to_user(data_vector=data_vector) ; input('Press any key...')
            elif method == 3:
                parser = helper.list_chats()
                current_chat_id = int(input('Enter the chat_id\n>>> '))
                add_members_in_chat(parser.users_group[current_chat_id][0], data_vector)
                input('Users adding...\nPress any key...')
            elif method == 4:
                print('Program finished...') ; input('Press any key...')
            else:
                print('Exception: wrong input. Try again') ; input('Press any key...')
            helper.clear_screen()
