import json

class Serializable():
    def __str__(self):
        return json.dumps(self.__dict__)
    

class Message(Serializable):
    def __init__(self, message=None):
        try:
            self.message = json.loads(message)["message"]
        except:
            self.message = message
            