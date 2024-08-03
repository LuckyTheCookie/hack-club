# An interface for the password generator using Custom Tkinter

import tkinter as tk
import customtkinter as ctk
from tkinter import messagebox
from tkinter import simpledialog
import random
import string
import os

dictionnary = os.path.join(os.path.dirname(__file__), 'words.txt')

def generate_password(length: int) -> str:
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def generate_passphrase(words: int) -> str:
    # Ouvrir le dictionnaire de mots, ajouter un chiffre aléatoire et un tiret entre chaque mot
    if words < 4:
        messagebox.showwarning("Warning", "Passphrases should be at least 4 words long for security reasons.")
        return
    with open(dictionnary, 'r') as file:
        word_list = file.readlines()
    passphrase = ''
    for i in range(words):
        passphrase += random.choice(word_list).strip() + str(random.randint(0, 9)) + '-'
    return passphrase.strip()

def generate_password_callback():
    length = simpledialog.askinteger("Password Length", "Enter the length of the password:")
    if length:
        password = generate_password(length)
        messagebox.showinfo("Password", f"Your password is: {password}")
    
def generate_passphrase_callback():
    words = simpledialog.askinteger("Passphrase Words", "Enter the number of words in the passphrase:")
    if words:
        passphrase = generate_passphrase(words)
        messagebox.showinfo("Passphrase", f"Your passphrase is: {passphrase}")

def main():
    root = tk.Tk()
    root.title("Password Generator")
    
    password_button = ctk.CTkButton(root, text="Generate a random password", command=generate_password_callback)
    password_button.pack(pady=10)

    passphrase_button = ctk.CTkButton(root, text="Generate a passphrase", command=generate_passphrase_callback)
    passphrase_button.pack(pady=10)
    
    root.mainloop()

if __name__ == '__main__':
    main()
    