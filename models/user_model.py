"""
user_model deals with user data,bussiness logic and connection to 
databases(database actions) or firebase for authentication tasks.

User data which is retervied from firebase
contains user-creation and user-login logic
along with data and it also contains user creation,login and logout logic
with help of firebase.d

"""

import os
import pyrebase

from constants import FILE_NAME
from utils.utils import Utils

class UserModel:
    def __init__(self):
        self.config = {
                "apiKey": "AIzaSyBSUAOmBsMv01ZTNqEv0K7tgEFgXCQhRbw",
                "authDomain": "eye-tracker-8943a.firebaseapp.com",
                "projectId": "eye-tracker-8943a",
                "databaseURL" : "https://eye-tracker-8943a.firebaseio.com",
                "storageBucket": "eye-tracker-8943a.appspot.com",
                "messagingSenderId": "261943693038",
                "appId": "1:261943693038:web:eb4621866673e76e0cadff"
                };      
        self.firebase = pyrebase.initialize_app(self.config)
        self.auth = self.firebase.auth()
        self.utils = Utils()


    def create_user_and_send_verif_mail(self,email,password):
        try:
            user = self.auth.create_user_with_email_and_password(email, password)
            self.send_verfication_mail(user)
            return True,user
        except Exception as e:
            error_message = str(e)
            print("create_user: ",error_message)

            if "WEAK_PASSWORD" in error_message:
                err_msg = "Password should be at least 6 characters."
                print("Exception create_user_and_send_verif_mail: ",err_msg)
                return False,err_msg
            elif "INVALID_EMAIL" in error_message:
                err_msg = "Invalid email"
                print("Exception create_user_and_send_verif_mail: ",err_msg)
                return False,err_msg
            elif "INVALID_PASSWORD" in error_message:
                err_msg = "Invalid password"
                print("Exception create_user_and_send_verif_mail: ",err_msg)
                return False,err_msg
            elif "USER_NOT_FOUND" in error_message:
                err_msg = "User not found"
                print("Exception create_user_and_send_verif_mail: ",err_msg)
                return False,err_msg
            else:
                err_msg = "An error occurred"
                print("Exception create_user_and_send_verif_mail: ",err_msg)
                return False,err_msg

    
    def login_user_and_chk_mail_verif(self,email,password):
        try:
            user = self.auth.sign_in_with_email_and_password(email, password)
            self.check_mail_verfication(user)
            # Saves the login credentails locally, so as to avoid logging in again
            # every time when application opens.
            # Log in credentails are saved in a file with ecryption such that one 
            # can read/understand/decrypt the data/file except, application.
            self.utils.encrypt_token_and_save(user['idToken'])
            return True,user
        except Exception as e:
            error_message = str(e)
            print("login_user_and_chk_mail_verif: ", error_message)

            if "INVALID_EMAIL" in error_message:
                err_msg = "Invalid email format. Please enter a valid email."
                print("Exception login_user_and_chk_mail_verif: ",err_msg)
                return False,err_msg
            elif "USER_DISABLED" in error_message:
                err_msg = "User account has been disabled. Please contact support."
                print("Exception login_user_and_chk_mail_verif: ",err_msg)
                return False,err_msg
            elif "USER_NOT_FOUND" in error_message:
                err_msg = "User not found. Please check your email."
                print("Exception login_user_and_chk_mail_verif: ",err_msg)
                return False,err_msg
            elif "INVALID_PASSWORD" in error_message:
                err_msg = "Invalid password. Please try again."
                print("Exception login_user_and_chk_mail_verif: ",err_msg)
                return False,err_msg
            elif "INVALID_LOGIN_CREDENTIALS" in error_message:
                err_msg = "Invalid credentials. Please try again."
                print("Exception login_user_and_chk_mail_verif: ",err_msg)
                return False,err_msg
            elif "EMAIL_EXISTS" in error_message:
                err_msg = "Email already exits. Please use different email."
                print("Exception login_user_and_chk_mail_verif: ",err_msg)
                return False,err_msg
            elif "EMAIL_NOT_VERIFIED" in error_message:
                err_msg = "Email not verified. Please verify email."
                print("Exception login_user_and_chk_mail_verif: ",err_msg)
                return False,err_msg
            else:
                err_msg = "An error occurred"
                print(err_msg)
                return False, err_msg
            

    def send_verfication_mail(self,user):
        user_token = user['idToken']
        if user_token:
            self.auth.send_email_verification(user_token)

    def check_mail_verfication(self,user):
        user_data = self.auth.get_account_info(user['idToken'])
        is_mail_verified = user_data['users'][0]['emailVerified']
        if is_mail_verified:
            return True
        else:
            raise Exception("EMAIL_NOT_VERIFIED")
        
    def verify_token(self,token):
        try:
            self.auth.get_account_info(token)
            return True
        except Exception as e:
            print("Exception verify_token: ",e)
            return False
    
    def logout(self):
        try:
            # Attempt to delete the file
            os.remove(FILE_NAME)
        except FileNotFoundError:
            raise FileNotFoundError 
        
    def set_username(self,user,username):
        self.auth.update_profile(id_token=user['idToken'],display_name=username)

    def get_username(self,id_token):
        user_info = self.auth.get_account_info(id_token)
        username = user_info['users'][0]['displayName']
        return username
