import tkinter as tk
from tkinter import messagebox
from tkinter import font
from PIL import Image, ImageTk
from pyautogui import sleep
import threading 
from controller.dashboard_controller import DashboardController
from services.eye_tracking import start_eye_tracking
from constants import *
import os

from utils.app_config import AppConfig
from utils.utils import Utils


class DashboardScreen:
    eye_tracking_active = False
    def __init__(self, master, go_back_callback, username, welcome_msg):
        self.dashboard_controller = DashboardController()
        self.master = master
        self.go_back_callback = go_back_callback
        self.username = username
        self.welcome_msg = welcome_msg
        self.utils = Utils()
        self.app_config = AppConfig(master)
        self.is_eye_tracking_active = False  # Flag to track eye tracking activation
        self.eye_tracking_thread = None  # Thread object for eye tracking

        self.dashboard_screen = tk.Toplevel(self.master)
        self.dashboard_screen.title(DASHBOARD_HEADER_TITLE)
        self.dashboard_screen.geometry(SCREEN_SIZE)
        self.dashboard_screen.resizable(False, False)

        self.font = self.app_config.APP_FONT

        # Title label
        self.title_label = tk.Label(self.dashboard_screen, text=DASHBOARD_TITLE + username + "!",
                                     font=self.app_config.TITLE_LABLE_FONT, )
        self.title_label.place(relx=0.5, y=30, anchor="center")

        # Greting label
        self.title_label = tk.Label(self.dashboard_screen,
                                     text="Hey " + self.utils.greet_user() + "." + self.welcome_msg,
                                     font=self.app_config.APP_FONT, )
        self.title_label.place(relx=0.5, y=80, anchor="center")

        # Instruction label
        self.title_label = tk.Label(self.dashboard_screen, text=DASHBOARD_AUTO_EYE_MOUSE_MESSAGE,
                                     font=self.app_config.APP_FONT)
        self.title_label.place(relx=0.5, y=150, anchor="center")

        # Load button images
        self.activate_image = Image.open(ON_IMAGE_PATH).resize((300, 100))
        self.deactivate_image = Image.open(OFF_IMAGE_PATH).resize((300, 100))

        # Set initial button image
        self.button_image = ImageTk.PhotoImage(self.deactivate_image)

        # Activate button
        self.image_button = tk.Button(self.dashboard_screen, image=self.button_image, command=self.toggle_eye_tracking)
        self.image_button.place(relx=0.5, rely=0.7, anchor="center")
        self.style_button(self.image_button)

        # Line
        self.line_canvas = tk.Canvas(self.dashboard_screen, width=WIDTH, height=2, bg="black", highlightthickness=0)
        self.line_canvas.place(relx=0.5, rely=0.9, anchor="center")

        # Status label
        self.status_label = tk.Label(self.dashboard_screen, text="Application is not running.",
                                      font=self.app_config.APP_FONT, fg="red", )
        self.status_label.place(relx=0.2, rely=0.95, anchor="center")

        # logout button
        self.logout_image = Image.open(LOGOUT_BT_IMAGE_PATH)
        self.logout_image = self.logout_image.resize((25, 30))
        self.lognout_img = ImageTk.PhotoImage(self.logout_image)
        self.logout_button = tk.Button(self.dashboard_screen, image=self.lognout_img, command=self.go_back)
        self.logout_button.place(relx=0.95, rely=0.95, anchor="center")
        self.style_button(self.logout_button)

        # info button
        self.info_image = Image.open(INFO_BT_IMAGE_PATH)
        self.info_image = self.info_image.resize((25, 30))
        self.info_img = ImageTk.PhotoImage(self.info_image)
        self.info_button = tk.Button(self.dashboard_screen, image=self.info_img, command=self.show_info_message)
        self.info_button.place(relx=0.88, rely=0.95, anchor="center")
        self.style_button(self.info_button)

        # customer care button
        self.cust_image = Image.open(CUSTOMER_BT_IMAGE_PATH)
        self.cust_image = self.cust_image.resize((25, 30))
        self.cust_img = ImageTk.PhotoImage(self.cust_image)
        self.cust_button = tk.Button(self.dashboard_screen, image=self.cust_img, command=self.show_contact_message)
        self.cust_button.place(relx=0.80, rely=0.95, anchor="center")
        self.style_button(self.cust_button)

    def style_button(self, button):
        button.config(font=self.font, bd=0, relief="flat", highlightthickness=0, highlightbackground="gray")

    def toggle_eye_tracking(self):
        self.is_eye_tracking_active = not self.is_eye_tracking_active  # Toggle the flag
        if self.is_eye_tracking_active:
            self.status_label.config(text="Application is running.", fg="green")
            self.animate_toggle(True)
            AppConfig.eye_tracking_active = not AppConfig.eye_tracking_active
            self.eye_tracking_thread = threading.Thread(target=start_eye_tracking)
            self.eye_tracking_thread.start()
        else:
            print("ET",AppConfig.eye_tracking_active)
            self.status_label.config(text="Application is not running", fg="red")
            self.animate_toggle(False)
            AppConfig.eye_tracking_active = not AppConfig.eye_tracking_active


    def animate_toggle(self, is_active):
        if is_active:
            self.button_image = ImageTk.PhotoImage(self.activate_image)
        else:
            self.button_image = ImageTk.PhotoImage(self.deactivate_image)
        self.image_button.config(image=self.button_image)
        self.master.update()

    def go_back(self):
        self.dashboard_controller.logout()
        self.dashboard_screen.destroy()  # Close the dashboard window
        self.go_back_callback()

    def show_info_message(self):
        messagebox.showinfo("About", INFO_MSG)

    def show_contact_message(self):
        messagebox.showinfo("Contact Information", CONTACT_MSG)


def call_back():
    print("dashboard")


if __name__ == "__main__":
    root = tk.Tk()
    signup_screen = DashboardScreen(root, call_back)
    root.mainloop()
