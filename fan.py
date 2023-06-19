class Fan:
    def __init__(self, username, token):
        self.username = username
        self.token = token

    def create_url(self):
        return "https://bandcamp.com/" + self.username
    
    def print(self):
        print({ 
            'username': self.username,
            'token': self.token
        })