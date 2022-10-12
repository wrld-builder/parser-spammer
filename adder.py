from config import app

def add_members_in_chat(chat_id, data_vector):
    if data_vector is not None:
        users_exists_id = []

        for member in app.get_chat_members(chat_id):
            users_exists_id.append(str(member.user.id))

        for data in data_vector:
            if str(data[0].split()[0]) not in users_exists_id:
                app.add_chat_members(chat_id, data[0].split()[0])
            else:
                continue
