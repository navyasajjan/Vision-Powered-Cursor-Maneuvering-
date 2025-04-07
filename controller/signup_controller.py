"""
signup_controller actually acts a middle component 
where view directly interacts with controller and controller  
interacts with model by invoking a method and gives the retireved 
data to view.


Has signup related functionalities.

"""

from models.user_model import UserModel


class SignupController:
    def __init__(self):
        self.user = UserModel()

    def signup_and_send_verif_mail(self,email,password):
        is_signed_up,data = self.user.create_user_and_send_verif_mail(email,password)
        if is_signed_up:
            return True,data
        else:
            return False,data
        
    def set_username(self,user,username):
        self.user.set_username(user,username)
