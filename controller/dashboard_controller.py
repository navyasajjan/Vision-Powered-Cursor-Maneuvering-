"""
dashboard_controller actually acts a middle component 
where view directly interacts with controller and controller  
interacts with model by invoking a method and gives the retireved 
data to view.


Has dashboard related functionalities.

"""

from constants import FILE_NAME
from models.user_model import UserModel


class DashboardController:
    def __init__(self):
        self.user = UserModel()

    def logout(self):
        try:
            self.user.logout()
        except FileNotFoundError as fne:
            print(f"Exception logout: ",fne)

