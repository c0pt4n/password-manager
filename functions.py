import random
import string
import pyperclip
import json
import tkinter as tk

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password(password_entry):
    letters = string.ascii_letters
    numbers = string.digits
    symbols = string.punctuation

    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)
    pyperclip.copy(password)
    password_entry.delete(0, tk.END)  # Use tk.END for cross-platform compatibility
    password_entry.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save(website_entry, email_entry, password_entry):
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showerror(title="Unacceptable Details", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            data = {}
        except json.decoder.JSONDecodeError:
            data = {}

        # dictionary to store emails and passwords in json format
        data.update({
            website: {
                "email": email,
                "password": password,
            }
        })
        with open("data.json", "w") as data_file:
            # Saving/Writing the data
            json.dump(data, data_file, indent=4)

            website_entry.delete(0, tk.END)
            password_entry.delete(0, tk.END)


def find_password(website_entry, password_entry):
    is_found = 0
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="No File Found", message="No Data File Found")
        data = {}
    except json.JSONDecodeError:
        messagebox.showinfo(title="No Data Found", message="data.json does not contain data")
        data = {}
    else:
        for key, value in data.items():
            if key == website_entry.get():
                messagebox.showinfo(title=website_entry.get(),
                                    message=f"Username: {key}\nPassword: {value['password']}")
                is_found = 1
                website_entry.delete(0, tk.END)
                password_entry.delete(0, tk.END)
        if is_found == 0:
            messagebox.showinfo(title="Error", message=f"No Details For {website_entry.get()} Found")
            website_entry.delete(0, tk.END)
            password_entry.delete(0, tk.END)
