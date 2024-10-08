# from controller.student_controller import StudentController
from tkinter import *
import tkinter.messagebox as msgbox
from view.component import EntryWithLabel
from view.teacher_view import TeacherView


class LoginTeacher:
    def __init__(self):
        self.window = Tk()
        self.window.title("Login Teacher")
        self.window.geometry("300x300")

        self.username = EntryWithLabel(self.window, "Username", 40, 60)
        self.password = EntryWithLabel(self.window, "Password", 40, 100)

        Label(self.window, text="* Don't have an account?", foreground="red").place(x=40,y=200)
        Button(self.window, text="Sign up", foreground= "red", width=7, command=TeacherView).place(x=185, y=198)

        Button(self.window, text="Login", width=10, command= self.login_click).place(x=102, y=150)

        self.window.mainloop()

    def login_click(self):
        print(self.username.get(), self.password.get())
        msgbox.showinfo("Login", "You have successfully logged in")
