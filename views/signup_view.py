import tkinter as tk
from tkinter import messagebox
from tkinter import font
from PIL import Image, ImageTk

from constants import *
from controller.signup_controller import SignupController
from utils.app_config import AppConfig

class SignupScreen:
    def __init__(self, master, go_back_callback):
        self.master = master
        self.signup_controller = SignupController()
        self.app_config  = AppConfig(master)
        self.go_back_callback = go_back_callback

        self.signup_screen = tk.Toplevel(self.master)
        self.signup_screen.title(SIGNUP_HEADER_TITLE)
        self.signup_screen.geometry(SCREEN_SIZE)
        self.signup_screen.resizable(False, False)
        
        self.font = self.app_config.APP_FONT

         # Load logo/picture
        self.logo_image = Image.open(LOGO_IMAGE_PATH) 
        self.logo_image = self.logo_image.resize((75, 75))
        self.logo_img = ImageTk.PhotoImage(self.logo_image)

        # Logo/picture label
        self.logo_label = tk.Label(self.signup_screen, image=self.logo_img)
        self.logo_label.place(relx=0.5, rely=0.1, anchor="center")

        # Title label
        self.title_label = tk.Label(self.signup_screen, text="SignUp", font=self.app_config.TITLE_LABLE_FONT, underline=True)
        self.title_label.place(relx=0.5, y=100, anchor="center")

        # Function to style buttons
        def style_button(button):
            button.config(font=self.font, bd=0, relief="flat", highlightthickness=2, highlightbackground="gray")

        # Username label and entry
        self.username_label = tk.Label(self.signup_screen, text="Username: ", font=self.font)
        self.username_label.place(relx=0.1, rely=0.4, anchor="center")
        self.username_entry = tk.Entry(self.signup_screen, font=self.font,fg="gray")
        self.username_entry.place(relx=0.35, rely=0.4, anchor="center")
        self.username_entry.insert(0,"navya sajjan")
        self.username_entry.bind("<FocusIn>",self.username_entry_focus_in)
        self.username_entry.bind("<FocusOut>",self.username_entry_focus_out)

        # Email label and entry
        self.email_label = tk.Label(self.signup_screen, text=" Email Id:", font=self.font)
        self.email_label.place(relx=0.55, rely=0.4, anchor="center")
        self.email_entry = tk.Entry(self.signup_screen, font=self.font,fg="gray")
        self.email_entry.place(relx=0.80, rely=0.4, anchor="center")
        self.email_entry.insert(0,"navya@gmail.com")
        self.email_entry.bind("<FocusIn>",self.email_entry_focus_in)
        self.email_entry.bind("<FocusOut>",self.email_entry_focus_out)

        # Password label and entry
        self.password_label = tk.Label(self.signup_screen, text="Password:", font=self.font)
        self.password_label.place(relx=0.2, rely=0.5, anchor="center")
        self.password_entry = tk.Entry(self.signup_screen, font=self.font, show="*",fg="gray")
        self.password_entry.place(relx=0.5, rely=0.5, anchor="center")
        self.password_entry.insert(0,"password")
        self.password_entry.bind("<FocusIn>",self.password_entry_focus_in)
        self.password_entry.bind("<FocusOut>",self.password_entry_focus_out)

         # Confirm password label and entry
        self.confirm_password_label = tk.Label(self.signup_screen, text="Confirm Password: ", font=self.font)
        self.confirm_password_label.place(relx=0.2, rely=0.6, anchor="center")
        self.confirm_password_entry = tk.Entry(self.signup_screen, font=self.font, show="*",fg="gray")
        self.confirm_password_entry.place(relx=0.5, rely=0.6, anchor="center")
        self.confirm_password_entry.insert(0,"password")
        self.confirm_password_entry.bind("<FocusIn>",self.confirm_password_entry_focus_in)
        self.confirm_password_entry.bind("<FocusOut>",self.confirm_password_entry_focus_out)
        
        # Checkbutton 
        self.check_box_var = tk.BooleanVar()
        self.terms_checkbox = tk.Checkbutton(self.signup_screen, text="I agree to use the application and follow netiquette rules.", variable=self.check_box_var,font=self.app_config.APP_FONT)
        self.terms_checkbox.place(relx=0.5, rely=0.7, anchor="center") 

        # Signup button
        self.signup_image = Image.open(SIGNUP_BT_IMAGE_PATH)
        self.signup_image = self.signup_image.resize((150, 40))
        self.signup_img = ImageTk.PhotoImage(self.signup_image)
        self.signup_button = tk.Button(self.signup_screen, image=self.signup_img, command=self.signup)
        self.signup_button.place(relx=0.5, rely=0.85, anchor="center") 
        style_button(self.signup_button)

        # Back button
        self.back_image = Image.open(BACK_BT_IMAGE_PATH)
        self.back_image = self.back_image.resize((50, 50))
        self.back_img = ImageTk.PhotoImage(self.back_image)
        self.back_button = tk.Button(self.signup_screen, image=self.back_img, command=self.go_back)
        self.back_button.place(relx=0.05, rely=0.9, anchor="center")  
        style_button(self.back_button)

    def username_entry_focus_in(self,event):
        if self.username_entry.get() == "navya sajjan":
            self.username_entry.delete(0,'end')
            self.username_entry.config(fg="black",highlightcolor="green",highlightthickness=2,highlightbackground="green")

    def username_entry_focus_out(self,event):
        if self.username_entry.get() == "":
            self.username_entry.insert(0,"navya sajjan")
            self.username_entry.config(fg="gray",highlightcolor="red",highlightthickness=2,highlightbackground="red")
        if self.username_entry.get() == "navya sajjan":
            self.username_entry.config(highlightcolor="red",highlightthickness=2,highlightbackground="red")

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

    def confirm_password_entry_focus_in(self,event):
        if self.confirm_password_entry.get() == "password":
            self.confirm_password_entry.delete(0,'end')
            self.confirm_password_entry.config(fg="black",highlightcolor="green",highlightthickness=2,highlightbackground="green")

    def confirm_password_entry_focus_out(self,event):
        if self.confirm_password_entry.get() == "":
            self.confirm_password_entry.insert(0,"password")
            self.confirm_password_entry.config(fg="gray",highlightcolor="red",highlightthickness=2,highlightbackground="red")
        
        if self.confirm_password_entry.get() == "password":
            self.confirm_password_entry.config(highlightcolor="red",highlightthickness=2,highlightbackground="red")


    def signup(self):
        username = self.username_entry.get()
        email = self.email_entry.get()
        password = self.password_entry.get()
        confirm_password = self.confirm_password_entry.get()
        is_checked = self.check_box_var.get()
        
        if not username and  not email and not password:
            messagebox.showerror("Error", "Please enter username,email and password.") 
        elif not username:
            messagebox.showerror("Error", "Please enter username.") 
        elif not email:
            messagebox.showerror("Error", "Please enter email.") 
        elif not password:
            messagebox.showerror("Error", "Please enter password.") 
        elif password != confirm_password:
            messagebox.showerror("Error", "Passwords do not match!")
        elif not is_checked:
            messagebox.showerror("Error", "Please agree terms of use.")
        else:
            is_signed_up,data = self.signup_controller.signup_and_send_verif_mail(email,password)
            if is_signed_up:
                messagebox.showinfo("Successful","Congrats!.You have successfully signed up. Please verify email and login now")
                self.signup_controller.set_username(data,username)
                self.go_back()
            else:
                messagebox.showerror("error",data)
            
    def go_back(self):
        self.signup_screen.destroy()  # Close the signup screen
        self.go_back_callback()  # Call the callback to go back to the main screen

def call_back():
    print("hello")

# Uncomment the following lines for standalone testing
# if __name__ == "__main__":
#     root = tk.Tk()
#     signup_screen = SignupScreen(root,call_back)
#     root.mainloop()
