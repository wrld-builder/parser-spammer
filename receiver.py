class Receiver:
    def __init__(self):
        self.data_vector = []

    def recognize_data(self, path_to_data):
        with open(str(path_to_data), mode='r', encoding='utf-8') as file:
             for line in file.readlines():
                 r_element = '\n'
                 self.data_vector.append([line.rstrip(r_element)])
        print(self.data_vector)
        return self.data_vector
