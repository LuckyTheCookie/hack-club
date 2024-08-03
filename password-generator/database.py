# Save the password to the a sqlite database

import sqlite3
import os

database = os.path.join(os.path.dirname(__file__), 'passwords.db')

def create_database():
    # Create a database PASSWORDS with a table PASSWORDS, EMAILS and a column id
    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS CREDENTIALS
                        (id INTEGER PRIMARY KEY, password TEXT, website TEXT, email TEXT)''')
    conn.close()
    print("Database created successfully.")

def save_password(password, website, email):
    # Save the password to the database
    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO CREDENTIALS (password, website, email) VALUES (?, ?, ?)''', (password, website, email))
    conn.commit()
    conn.close()

def search_in_database(website):
    # Search the database for the website and display all the passwords saved for that website
    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM CREDENTIALS WHERE website = ?''', (website,))
    results = cursor.fetchall()
    conn.close()
    if results:
        for result in results:
            print(f"Password: {result[1]}\nEmail: {result[3]}\nWebsite: {result[2]}\n")
    else:
        print("No passwords found for this website.")
