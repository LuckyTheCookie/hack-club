# This file is being co-written with Github Copilot
# This is a simple password generator that generates a random password of a specified length or a passphrase of a specified number of words

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
        print("Warning: Passphrases should be at least 4 words long for security reasons.")
        return
    with open(dictionnary, 'r') as file:
        word_list = file.readlines()
    passphrase = ''
    for i in range(words):
        passphrase += random.choice(word_list).strip() + str(random.randint(0, 9)) + '-'
    return passphrase.strip()



def main():
    print("Welcome to the Password Generator!")
    print("1. Generate a random password")
    print("2. Generate a passphrase")
    choice = input("Enter your choice (1/2): ")
    if choice == '1':
        length = int(input("Enter the length of the password: "))
        password = generate_password(length)
        print(f"Your password is: {password}")
    elif choice == '2':
        words = int(input("Enter the number of words in the passphrase: "))
        passphrase = generate_passphrase(words)
        print(f"Your passphrase is: {passphrase}")
    else:
        print("Invalid choice. Please enter 1 or 2.")

if __name__ == '__main__':
    main()