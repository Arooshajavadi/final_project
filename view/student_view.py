from tkinter import *
import tkinter.messagebox as msgbox
from view.component import EntryWithLabel



class StudentView:
    def __init__(self):
        self.window = Tk()
        self.window.title("Student Profile")
        self.window.geometry("450x500")

        self.id = EntryWithLabel(self.window,"ID", 40, 60, variable_type=IntVar)
        self.name = EntryWithLabel(self.window,"Name", 40, 120)
        self.family = EntryWithLabel(self.window,"Family", 40, 180)
        self.username = EntryWithLabel(self.window,"Username", 40, 240)
        self.password = EntryWithLabel(self.window,"Password", 40, 300)
        self.phone = EntryWithLabel(self.window,"Phone", 40, 360, variable_type=IntVar)
        self.grade = EntryWithLabel(self.window,"Email", 40, 420, variable_type=IntVar)

        Label(self.window, text="Are you sure about the information?", font=["Arial", 8], foreground="darkblue").place(x=40, y=440)
        self.x = IntVar()
        Radiobutton(self.window, text="yes", font=["Arial",8], foreground="darkblue",variable=self.x, value=1).place(x=260, y=440)
        self.x.set(0)

        Button(self.window, text="", width=6).place(x=40, y=460)
        Button(self.window, text="", width=6).place(x=110, y=460)
        Button(self.window, text="", width=6).place(x=180, y=460)


        self.window.mainloop()
