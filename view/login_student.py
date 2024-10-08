from tkinter import *
# from controller.student_controller import StudentController
import tkinter.messagebox as msgbox
from view.component import EntryWithLabel

class LoginStudent:
    def __init__(self):
        self.window = Tk()
        self.window.title("Login Student")
        self.window.geometry("250x300")

        self.username = EntryWithLabel(self.window, "Username", 20, 150)
        self.password = EntryWithLabel(self.window, "Password", 20, 190)

        Button(self.window, text="Login", width=10, command= self.login_click).place(x=80, y=250)

        self.window.mainloop()

    def login_click(self):
        print(self.username.get(), self.password.get())
        msgbox.showinfo("Login", "You have successfully logged in")