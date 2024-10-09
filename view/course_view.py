from tkinter import *
import tkinter.messagebox as msgbox
from controller.course_controller import CourseController
from view.component import EntryWithLabel




class CourseView:
    def __init__(self):
        self.window = Tk()
        self.window.title("Select Course")
        self.window.geometry("500x500")


        self.id = EntryWithLabel(self.window, "ID", 40, 60, variable_type=IntVar)
        self.username = EntryWithLabel(self.window, "Username", 40, 120)
        self.password = EntryWithLabel(self.window, "Password", 40, 180)
        self.title = EntryWithLabel(self.window, "Title", 40, 240)
        self.teacher = EntryWithLabel(self.window, "Teacher", 40, 300)
        self.code = EntryWithLabel(self.window, "Code", 40, 360, variable_type=IntVar)

        Label(self.window, text="Are you sure about enrolling in this class?", font=["Arial", 8], foreground="darkblue").place(x=40, y=400)
        self.x = IntVar()
        Radiobutton(self.window, text="yes", font=["Arial",8], foreground="darkblue",variable=self.x, value=1).place(x=260, y=400)
        self.x.set(0)

        Button(self.window, text = "Save", width = 7, command= self.save_click).place(x=40, y=430)
        Button(self.window, text = "Edit", width = 7, command= self.edit_click).place(x=110, y=430)
        Button(self.window, text = "Remove", width = 7, command= self.remove_click).place(x=180, y=430)


        self.window.mainloop()

    def save_click(self):
        if self.x.get() == 1:
            CourseController.save(self.id.get(), self.username.get(), self.password.get(), self.title.get(), self.teacher.get(), self.code.get())
            self.reset()
            msgbox.showinfo("Save", "Saved Successfully")
        else:
            msgbox.showerror("Error", "Please press the yes button first")



    def edit_click(self):
        if self.x.get() == 1:
            CourseController.edit(self.id.get(), self.username.get(), self.password.get(), self.title.get(), self.teacher.get(), self.code.get())
            self.reset()
            msgbox.showinfo("Edit", "Edited Successfully")
        else:
            msgbox.showerror("Error", "Please press the yes button first")

    def remove_click(self):
        CourseController.remove(self.id.get())
        self.reset()
        msgbox.showinfo("Remove", "Removed Successfully")


    def reset(self):
        self.id.set(0)
        self.username.set("")
        self.password.set("")
        self.title.set("")
        self.teacher.set("")
        self.code.set(0)

