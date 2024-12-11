from tkinter import *
from functions import generate_password, save, find_password

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)

main_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=main_image)
canvas.grid(column=1, row=0)

website_label = Label(text="Website: ")
website_label.grid(column=0, row=1)

website_entry = Entry(width=35)
website_entry.grid(column=1, row=1)
website_entry.focus()

website_search_btn = Button(text="Search", command=lambda: find_password(website_entry=website_entry, password_entry=password_entry))
website_search_btn.grid(column=2, row=1, sticky="EW")

email_label = Label(text="Email/Username: ")
email_label.grid(column=0, row=2)

email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2, sticky="EW")
email_entry.insert(0, "Enter your mail")  # END represents the last character of the entry ie.., the cursor will
# be at the end of the entry for you to edit. Or you can use 0 which represents the beginning of the entry

password_label = Label(text="Password: ")
password_label.grid(column=0, row=3)

password_entry = Entry(width=21, show="*")
password_entry.grid(column=1, row=3, sticky="EW")

generate_password_btn = Button(text="Generate Password", command=lambda: generate_password(password_entry=password_entry))
generate_password_btn.grid(column=2, row=3, sticky="EW")

add_btn = Button(text="Add", width=36, command=lambda: save(website_entry=website_entry, email_entry=email_entry, password_entry=password_entry))
add_btn.grid(column=1, row=4, columnspan=2, sticky="EW")

window.mainloop()
