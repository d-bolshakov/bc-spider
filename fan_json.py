import json

class Fan:
    def __init__(self, username, token):
        self.username = username
        self.token = token

    def create_url(self):
        return "https://bandcamp.com/" + self.username
    
    def save_to_json(self, filename):
        fan_dict = { 'username': self.username, 'token': self.token }
        with open(filename, 'r') as file:
            json_object = json.load(file)
            print(json_object)