"""
login_controller actually acts a middle component 
where view directly interacts with controller and controller  
interacts with model by invoking a method and gives the retireved 
data to view.


Has login related functionalities.

"""
from models.user_model import UserModel


class LoginController:
    def __init__(self):
        self.user = UserModel()

    def login_and_chk_mail_verif(self,email,password):
        is_logged_in,data = self.user.login_user_and_chk_mail_verif(email,password)
        if is_logged_in:
            return True,data
        else:
            return False,data
        
    
    def get_username(self,id_token):
        return self.user.get_username(id_token)