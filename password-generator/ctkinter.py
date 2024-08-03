# An interface for the password generator using Custom Tkinter

import tkinter as tk
import customtkinter
from tkinter import messagebox
from tkinter import simpledialog
import random
import string
import os
from app import generate_password, generate_passphrase

dictionnary = os.path.join(os.path.dirname(__file__), 'words.txt')

app = customtkinter.CTk()
app.geometry("400x300")
app.title("Password Generator")





def change_view_password():
    # Wipe the screen and display the password generation form
    title.pack_forget()
    password_button.pack_forget()
    passphrase_button.pack_forget()
    length_label = customtkinter.CTkLabel(app, text="Enter the length of the password:")
    length_label.pack()
    length_entry = customtkinter.CTkEntry(app)
    length_entry.pack()
    generate_button = customtkinter.CTkButton(app, text="Generate", command=lambda: generate_password_view(length_entry.get()))
    generate_button.pack()
    
def change_view_passphrase():
    # Wipe the screen and display the passphrase generation form
    title.pack_forget()
    password_button.pack_forget()
    passphrase_button.pack_forget()
    words_label = customtkinter.CTkLabel(app, text="Enter the number of words in the passphrase:")
    words_label.pack()
    words_entry = customtkinter.CTkEntry(app)
    words_entry.pack()
    generate_button = customtkinter.CTkButton(app, text="Generate", command=lambda: generate_passphrase_view(words_entry.get()))
    generate_button.pack()

def classic_view():
    # Wipe the screen and display the classic interface
    title.pack()
    password_button.pack()
    passphrase_button.pack()

def generate_password_view(length):
    try:
        length = int(length)
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter a valid number.")
        return
    password = generate_password(length)
    messagebox.showinfo("Password generated and copied to clipboard", f"Your password is: {password}")
    hide_current_view()
    copy_password(password)
    classic_view()

def hide_current_view():
    for widget in app.winfo_children():
        widget.pack_forget()

def generate_passphrase_view(words):
    try:
        words = int(words)
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter a valid number.")
        return
    passphrase = generate_passphrase(words)
    messagebox.showinfo("Passphrase generated and copied to clipboard", f"Your passphrase is: {passphrase}")
    hide_current_view()
    copy_passphrase(passphrase)
    classic_view()

def copy_passphrase(passphrase):
    app.clipboard_clear()
    app.clipboard_append(passphrase)

def copy_password(password):
    app.clipboard_clear()
    app.clipboard_append(password)

title = customtkinter.CTkLabel(app, text="Welcome to the Password Generator!", font=("Arial", 16))
title.pack()

password_button = customtkinter.CTkButton(app, text="Generate a random password", command=change_view_password)
password_button.pack()

passphrase_button = customtkinter.CTkButton(app, text="Generate a passphrase", command=change_view_passphrase)
passphrase_button.pack()

app.mainloop()