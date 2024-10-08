from cgitb import reset
from tkinter import *
import tkinter.messagebox as msgbox
from view.component import EntryWithLabel



class TeacherView:
    def __init__(self):
        self.window = Tk()
        self.window.title("Teacher Profile")
        self.window.geometry("450x500")

        self.id = EntryWithLabel(self.window,"Teacher", 40, 60, variable_type=IntVar)
        self.name = EntryWithLabel(self.window,"Name", 40, 120)
        self.family = EntryWithLabel(self.window,"Family", 40, 180)
        self.username = EntryWithLabel(self.window,"Username", 40, 240)
        self.password = EntryWithLabel(self.window,"Password", 40, 300)
        self.phone = EntryWithLabel(self.window,"Phone", 40, 360)
        self.skill = EntryWithLabel(self.window,"Skill", 40, 420)

        Label(self.window, text="Are you sure about the information?", font=["Arial", 8], foreground="darkblue").place(x=40, y=440)
        self.x = IntVar()
        Radiobutton(self.window, text="yes", font=["Arial", 8], foreground="darkblue", variable=self.x, value=1).place(x=260, y=440)
        self.x.set(0)

        Button(self.window, text="Save", width=6, command=self.save_click).place(x=40, y=460)
        Button(self.window, text="Edit", width=6, command=self.edit_click).place(x=110, y=460)
        Button(self.window, text="Remove", width=6, command=self.remove_click).place(x=180, y=460)

        self.window.mainloop()

    def reset(self):
        self.id.set(0)
        self.name.set("")
        self.family.set("")
        self.username.set("")
        self.password.set("")
        self.phone.set(0)
        self.skill.set("")
        

    def save_click(self):
        if self.x.get() == 1:
            print(self.id.get(), self.name.get(), self.family.get(), self.username.get(), self.password.get(),self.phone.get(), self.skill.get())
            self.reset()
            msgbox.showinfo(title="Save", message="Saved Successfully")
        else:
            msgbox.showerror(title="Save", message="Please enter correct information")

    def edit_click(self):
        if self.x.get() == 1:
            print(self.id.get(), self.name.get(), self.family.get(), self.username.get(), self.password.get(),self.phone.get(), self.skill.get())
            self.reset()
        else:
            msgbox.showerror(title="Edit", message="Please enter correct information")

    def remove_click(self):
        if self.x.get() == 1:
            msgbox.showinfo(title="Remove", message="Removed Successfully")
            reset()
        else:
            msgbox.showerror(title="Remove", message="Please enter correct information")