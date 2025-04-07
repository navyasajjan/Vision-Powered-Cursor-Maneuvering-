from models.user_model import UserModel


class MainController():
    def __init__(self):
        self.user = UserModel()
    
    def get_username(self,id_token):
        return self.user.get_username(id_token=id_token)
