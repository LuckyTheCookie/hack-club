# An interface for the password generator using Custom Tkinter

import tkinter as tk
import customtkinter
from tkinter import messagebox
from tkinter import simpledialog
import random
import string
import os
from app import generate_password, generate_passphrase
from database import create_database, save_password, search_in_database

dictionnary = os.path.join(os.path.dirname(__file__), 'words.txt')
create_database()

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
    save_button.pack()

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

def database_view():
    # Wipe the screen and display the database interface
    # The user can save a password, email and website to the database, but also view all the passwords saved in the database
    hide_current_view()
    back_button = customtkinter.CTkButton(app, text="Back", command=classic_view)
    back_button.pack()
    database_title = customtkinter.CTkLabel(app, text="Database", font=("Arial", 16))
    database_title.pack()

    password_label = customtkinter.CTkLabel(app, text="Enter the password:")
    password_label.pack()
    password_entry = customtkinter.CTkEntry(app)
    password_entry.pack()

    email_label = customtkinter.CTkLabel(app, text="Enter the email:")
    email_label.pack()
    email_entry = customtkinter.CTkEntry(app)
    email_entry.pack()

    website_label = customtkinter.CTkLabel(app, text="Enter the website:")
    website_label.pack()
    website_entry = customtkinter.CTkEntry(app)
    website_entry.pack()

    save_button = customtkinter.CTkButton(app, text="Save", command=lambda: save_to_database(password_entry.get(), email_entry.get(), website_entry.get()))
    save_button.pack()

    # Add a divider, a search bar and a list of all the passwords saved in the database based on the website searched
    divider = customtkinter.CTkLabel(app, text="----------------------")
    divider.pack()
    search_label = customtkinter.CTkLabel(app, text="Search for a website:")
    search_label.pack()
    search_entry = customtkinter.CTkEntry(app)
    search_entry.pack()
    search_button = customtkinter.CTkButton(app, text="Search", command=lambda: search_database(search_entry.get()))
    search_button.pack()

def save_to_database(password, email, website):
    save_password(password, email, website)
    messagebox.showinfo("Password saved successfully", "Your password has been saved to the database.")

def search_database(website):
    # Search the database for the website and display all the passwords saved for that website
    print(website)
    search_in_database(website)


title = customtkinter.CTkLabel(app, text="Welcome to the Password Generator!", font=("Arial", 16))
title.pack()

password_button = customtkinter.CTkButton(app, text="Generate a random password", command=change_view_password)
password_button.pack()

passphrase_button = customtkinter.CTkButton(app, text="Generate a passphrase", command=change_view_passphrase)
passphrase_button.pack()

save_button = customtkinter.CTkButton(app, text="Access database", command=database_view)
save_button.pack()



app.mainloop()