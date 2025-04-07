import tkinter as tk
from tkinter import PhotoImage, font as fnt, messagebox
from PIL import Image, ImageTk
from constants import *
from controller.main_controller import MainController
from models.user_model import UserModel
from utils.app_config import AppConfig
from utils.utils import Utils
from views.dashboard_view import DashboardScreen
from views.login_view import LoginScreen
from views.signup_view import SignupScreen

def open_login_screen():
    root.withdraw()
    login_screen = LoginScreen(root, go_back_to_main_screen)

def go_back_to_main_screen():
    root.deiconify()  # Show the main screen

def open_signup_screen():
    root.withdraw()
    signup_screen = SignupScreen(root, go_back_to_main_screen)

# Create the main application window
root = tk.Tk()
root.title(HEADER_TITLE)
root.geometry(SCREEN_SIZE)
root.resizable(False, False)  # Make the window not resizable
# Application Icon
app_icon = PhotoImage(file = APP_ICON)
root.iconphoto(True,app_icon)

utils = Utils()
user = UserModel()
app_config = AppConfig(root)

is_file_exists, token = utils.decrypt_token()
is_valid_token = user.verify_token(token) if is_file_exists else False

if is_file_exists and is_valid_token:
    # Open the dashboard screen directly
    main_controller = MainController()
    username = main_controller.get_username(token)
    dashboard = DashboardScreen(root, go_back_to_main_screen,username,WELCOME_BACK_MSG)

# Load Roboto font
# font = fnt.Font(family="Times New Roman")
font = app_config.APP_FONT

# Title label
title_label = tk.Label(root, text=MAIN_TITLE, font=app_config.TITLE_LABLE_FONT)
title_label.place(relx=0.5, y=30, anchor="center")


# Load logo/picture
logo_image = Image.open(LOGO_IMAGE_PATH) 
logo_image = logo_image.resize((75, 75))  
logo_img = ImageTk.PhotoImage(logo_image)

# Logo/picture label
logo_label = tk.Label(root, image=logo_img)
logo_label.place(relx=0.5, rely=0.3, anchor="center")

# Function to style buttons
def style_button(button):
    button.config(font=font, bd=0, relief="flat", highlightthickness=2, highlightbackground="gray")

# Load images
login_image = Image.open(LOGIN_BT_IMAGE_PATH)
login_image = login_image.resize((150, 40))
login_img = ImageTk.PhotoImage(login_image)

signup_image = Image.open(SIGNUP_BT_IMAGE_PATH)
signup_image = signup_image.resize((150, 40))
signup_img = ImageTk.PhotoImage(signup_image)

# Login button
login_button = tk.Button(root, image=login_img, command=open_login_screen)
login_button.place(relx=0.5, rely=0.5, anchor="center")
style_button(login_button)

# Signup button
signup_button = tk.Button(root, image=signup_img, command=open_signup_screen)
signup_button.place(relx=0.5, rely=0.65, anchor="center")
style_button(signup_button)

# Made by team Navya text
bottom_label = tk.Label(root, text=TEAM_CREDITS, font=("Roboto", 8, "bold"))
bottom_label.place(relx=0.5, rely=0.95, anchor="center")

# Hide the main screen
if is_file_exists and is_valid_token:
    root.withdraw()

# Run the main event loop
root.mainloop()