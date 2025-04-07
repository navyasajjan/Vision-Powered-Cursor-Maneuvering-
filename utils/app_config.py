from tkinter import font


class AppConfig:
    eye_tracking_active = False
    def __init__(self,root):
        self.root = root
        self.APP_FONT = font.Font(family="Times New Roman")
        self.TITLE_LABLE_FONT = font.Font(family='Times New Roman',size=25,underline=1) 