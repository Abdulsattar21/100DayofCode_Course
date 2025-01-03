from tkinter import *

# ---------------------------- SAVE PASSWORD ------------------------------- #
# Here you can write from entry into files and these stuff
def save():
    pass
# ---------------------------- UI SETUP ------------------------------- #
from pandas import wide_to_long

window = Tk()
window.title("MyPass")
window.config(padx= 50, pady= 50)

canvas = Canvas(height=200, width=200)
log_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image= log_img)

canvas.grid(row=0, column=1)


# Labels
website_label = Label(text="Website")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username")
email_label.grid(row=2, column=0)
password_label = Label(text="Password")
password_label.grid(row=3, column=0)

#Entries
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "abdalsattarpro@gmail.com")
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

# Buttons
generate_password_button = Button(text="Generate Password")
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=36)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()
