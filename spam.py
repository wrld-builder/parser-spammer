from config import app

class Spam:
    def __init__(self):
        self.text_to_spam = ''

    def spam_to_user(self, data_vector):
        for data in data_vector:
            app.send_message(data[0].split()[0], self.text_to_spam)

    def set_text_to_spam(self, text):
        self.text_to_spam = text
