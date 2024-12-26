import tkinter
from tkinter import *
from Playground import add

window = tkinter.Tk()
window.title("hello")
window.minsize(500, 300)

# Label
my_label = Label(text="Hello, I'm a Label!", font=("Arial", 24, "bold"))
my_label.pack()

my_label["text"] = "New Text"
my_label.config(text="New Text")

# Button
def button_clicked():
    my_label.config(text=input.get())


button = Button(text="Click Me", command= button_clicked)
button.pack()

# entry

input = Entry(width=10)
input.pack()




window.mainloop()
