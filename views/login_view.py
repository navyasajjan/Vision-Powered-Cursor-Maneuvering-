import tkinter as tk
from tkinter import Entry, Label, PhotoImage, messagebox
from tkinter import font
from PIL import Image, ImageTk
from constants import *
from controller.login_controller import LoginController

from utils.app_config import AppConfig
from views.dashboard_view import DashboardScreen

class LoginScreen:
    def __init__(self, master, go_back_callback):
        self.master = master
        self.app_config = AppConfig(master)
        self.login_controller = LoginController()
        self.go_back_callback = go_back_callback

        self.login_screen = tk.Toplevel(self.master)
        self.login_screen.title(LOGIN_HEADER_TITLE)
        self.login_screen.geometry(SCREEN_SIZE)
        self.login_screen.resizable(False, False)

        self.font = self.app_config.APP_FONT
        # Load logo/picture
        self.logo_image = Image.open(LOGO_IMAGE_PATH) 
        self.logo_image = self.logo_image.resize((75, 75))
        self.logo_img = ImageTk.PhotoImage(self.logo_image)

        # Logo/picture label
        self.logo_label = tk.Label(self.login_screen, image=self.logo_img)
        self.logo_label.place(relx=0.5, rely=0.1, anchor="center")

        # Title label
        self.title_label = tk.Label(self.login_screen, text="Login", font=self.app_config.TITLE_LABLE_FONT)
        self.title_label.place(relx=0.5, y=100, anchor="center")

        # Function to style buttons
        def style_button(button):
            button.config(font=self.font, bd=0, relief="flat", highlightthickness=2, highlightbackground="gray")

        # Email label and entry
        self.email_label = tk.Label(self.login_screen, text="Email Id: ", font=self.font)
        self.email_label.place(relx=0.5, rely=0.4, anchor="center")
        self.email_entry = tk.Entry(self.login_screen, font=self.font,fg="gray",highlightthickness=2)
        self.email_entry.place(relx=0.5, rely=0.5, anchor="center")
        self.email_entry.insert(0,"navya@gmail.com")
        self.email_entry.bind("<FocusIn>",self.email_entry_focus_in)
        self.email_entry.bind("<FocusOut>",self.email_entry_focus_out)

        # Password label and entry
        self.password_label = tk.Label(self.login_screen, text="Password: ", font=self.font)
        self.password_label.place(relx=0.5, rely=0.6, anchor="center")
        self.password_entry = tk.Entry(self.login_screen, font=self.font, show="*",fg="gray",highlightthickness=2)
        self.password_entry.place(relx=0.5, rely=0.7, anchor="center")
        self.password_entry.insert(0,"password")
        self.password_entry.bind("<FocusIn>",self.password_entry_focus_in)
        self.password_entry.bind("<FocusOut>",self.password_entry_focus_out)

        # Login button
        self.login_image = Image.open(LOGIN_BT_IMAGE_PATH)
        self.login_image = self.login_image.resize((150, 40))
        self.login_img = ImageTk.PhotoImage(self.login_image)
        self.login_button = tk.Button(self.login_screen, image=self.login_img, command=self.login)
        self.login_button.place(relx=0.5, rely=0.85, anchor="center")
        style_button(self.login_button)

        # Bind the <Return> key to the login function
        self.login_screen.bind('<Return>', lambda event: self.login())

        # Back button
        self.back_image = Image.open(BACK_BT_IMAGE_PATH)
        self.back_image = self.back_image.resize((50,50))
        self.back_img = ImageTk.PhotoImage(self.back_image)
        self.back_button = tk.Button(self.login_screen, image= self.back_img, command=self.go_back)
        self.back_button.place(relx=0.05, rely=0.9, anchor="center")
        style_button(self.back_button)

    def email_entry_focus_in(self,event):
        if self.email_entry.get() == "navya@gmail.com":
            self.email_entry.delete(0,'end')
            self.email_entry.config(fg="black",highlightcolor="green",highlightthickness=2,highlightbackground="green")

    def email_entry_focus_out(self,event):
        if self.email_entry.get() == "":
            self.email_entry.insert(0,"navya@gmail.com")
            self.email_entry.config(fg="gray",highlightcolor="red",highlightthickness=2,highlightbackground="red")
        if self.email_entry.get() == "navya@gmail.com":
            self.email_entry.config(highlightcolor="red",highlightthickness=2,highlightbackground="red")

    def password_entry_focus_in(self,event):
        if self.password_entry.get() == "password":
            self.password_entry.delete(0,'end')
            self.password_entry.config(fg="black")
            self.password_entry.config(fg="black",highlightcolor="green",highlightthickness=2,highlightbackground="green")


    def password_entry_focus_out(self,event):
        if self.password_entry.get() == "":
            self.password_entry.insert(0,"password")
            self.password_entry.config(fg="gray",highlightcolor="red",highlightthickness=2,highlightbackground="red")

        if self.password_entry.get() == "password":
            self.password_entry.config(highlightcolor="red",highlightthickness=2,highlightbackground="red")

    def login(self):
        email = self.email_entry.get()
        password = self.password_entry.get()
        if not email and not password:
            messagebox.showerror("Error", "Please enter both username/email and password.") 
        elif not email:
            messagebox.showerror("Error", "Please enter username/email.") 

        elif not password:
            messagebox.showerror("Error", "Please enter password.") 
        else:
            print("Logged in")
            is_logged_in,data = self.login_controller.login_and_chk_mail_verif(email,password)
            if is_logged_in:
                user = data
                self.open_dashboard_screen(user)
            else:
                error = data
                messagebox.showerror("error",error)

    def open_dashboard_screen(self,user):
        self.login_screen.withdraw() 
        user_name = self.login_controller.get_username(user['idToken'])
        dashboard = DashboardScreen(self.master, self.go_back,user_name,WELCOME_MSG)

    def go_back(self):
        self.login_screen.destroy()  # Close the login window
        self.go_back_callback()  # Call the callback to go back to the main screen
