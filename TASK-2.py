import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password(length):
    try:
        password_length = int(length)
        if password_length <= 0:
            raise ValueError("Password length must be greater than zero.")

        # Generate password
        password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=password_length))

        # Generate a random color for displaying the password
        color = "#{:02x}{:02x}{:02x}".format(random.randint(0, 112), random.randint(0, 75), random.randint(0, 255))

        return password, color

    except ValueError as e:
        messagebox.showerror("Error", str(e))
        return None, None

def generate_password_gui():
    def generate():
        length = length_entry.get()
        password, color = generate_password(length)
        if password and color:
            password_label.config(text=password, fg=color)

    root = tk.Tk()
    root.title("Password Generator")

    label = tk.Label(root, text="Enter password length:")
    label.pack(pady=40, padx=15)

    length_entry = tk.Entry(root)
    length_entry.pack(pady=10, padx=90)

    generate_button = tk.Button(root, text="Generate Password", command=generate)
    generate_button.pack(pady=10)

    password_label = tk.Label(root, text="", font=("Helvetica", 16), wraplength=300)
    password_label.pack(pady=20)

    root.mainloop()

generate_password_gui()