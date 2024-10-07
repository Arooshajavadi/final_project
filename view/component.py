from tkinter import *


class EntryWithLabel:
    def __init__(self, window, text, x, y, variable_type=StringVar, distance=70):
        Label(window, text=text).place(x=x, y=y)
        self.variable = variable_type()
        Entry(window, textvariable=self.variable).place(x=x+distance, y=y)

    def get(self):
        return self.variable.get()

    def set(self, value):
        self.variable.set(value)