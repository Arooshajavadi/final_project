from tkinter import *
import tkinter.messagebox as msgbox

from controller.student_controller import StudentController
from view.component import EntryWithLabel



class StudentView:
    def __init__(self):
        self.window = Tk()
        self.window.title("Student Profile")
        self.window.geometry("400x550")

        self.id = EntryWithLabel(self.window,"ID", 40, 60, variable_type=IntVar, width=30)
        self.name = EntryWithLabel(self.window,"Name", 40, 120, width=30)
        self.family = EntryWithLabel(self.window,"Family", 40, 180, width=30)
        self.username = EntryWithLabel(self.window,"Username", 40, 240, width=30)
        self.password = EntryWithLabel(self.window,"Password", 40, 300, width=30)
        self.phone = EntryWithLabel(self.window,"Phone", 40, 360, variable_type=IntVar, width=30)
        self.grade = EntryWithLabel(self.window,"Grade", 40, 420, variable_type=IntVar, width=30)

        Label(self.window, text="Are you sure about the information?", font=["Arial", 8], foreground="darkblue").place(x=40, y=450)
        self.x = IntVar()
        Radiobutton(self.window, text="yes", font=["Arial",8], foreground="darkblue",variable=self.x, value=1).place(x=258, y=450)
        self.x.set(0)

        Button(self.window, text="Save", width=6, command=self.save_click).place(x=98, y=480)
        Button(self.window, text="Edit", width=6, command=self.edit_click).place(x=168, y=480)
        Button(self.window, text="Remove", width=6, command= self.remove_click).place(x=238, y=480)


        self.window.mainloop()

    def reset(self):
        self.id.set(0)
        self.name.set("")
        self.family.set("")
        self.username.set("")
        self.password.set("")
        self.phone.set(0)
        self.grade.set(0)


    def save_click(self):
        if self.x.get() == 0:
            StudentController.save(self.id.get(), self.name.get(), self.family.get(), self.username.get(), self.password.get(), self.phone.get(), self.grade.get())
            msgbox.showinfo("Save", "Saved Successfully")
            self.reset()
        else:
            msgbox.showerror("Error", "Please enter a valid information first")

    def edit_click(self):
        if self.x.get() == 0:
            StudentController.edit(self.id.get(), self.name.get(), self.family.get(), self.username.get(), self.password.get(), self.phone.get(), self.grade.get())
            msgbox.showinfo("Edit", "Edit Successfully")
            self.reset()
        else:
            msgbox.showerror("Error", "Please enter a valid information first")

    def remove_click(self):
        if self.x.get() == 0:
            StudentController.remove(self.id.get())
            msgbox.showinfo("Remove", "Removed successfully")
            self.reset()
        else:
            msgbox.showerror("Error", "Please enter a valid information first")

