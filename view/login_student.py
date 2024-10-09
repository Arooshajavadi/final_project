from controller.student_controller import StudentController
from tkinter import *
import tkinter.messagebox as msgbox
from view.component import EntryWithLabel
from view.course_view import CourseView
from view.login_teacher import LoginTeacher
from view.student_view import StudentView


class LoginStudent:
    def __init__(self):
        self.window = Tk()
        self.window.title("Login Student")
        self.window.geometry("300x300")

        self.username = EntryWithLabel(self.window, "Username", 40, 60)
        self.password = EntryWithLabel(self.window, "Password", 40, 100)

        Label(self.window, text="* Don't have an account?", foreground="red").place(x=40,y=200)
        Button(self.window, text="Sign up", foreground= "red", width=7, command=StudentView).place(x=185, y=198)
        Label(self.window, text="* Login as a teacher?", foreground="red").place(x=40,y=232)
        Button(self.window, text="Login", foreground="red", width=7, command=LoginTeacher).place(x=185, y=230)

        Button(self.window, text="Login", width=10, command= self.login_click).place(x=102, y=150)

        self.window.mainloop()

    def login_click(self):
        StudentController.find_by_username_and_password(self.username.get(), self.password.get())
        if True:
            msgbox.showinfo("Login", "You have successfully logged in")
            CourseView()