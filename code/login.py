import sqlite3
import logging
import tkinter as tk
from SystemLogger import SystemLogger

sl = SystemLogger()

def create_db():
    """Erstellt die SQLite-Datenbank und die Benutzer-Tabelle."""
    conn = sqlite3.connect('databases/users.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY,
            password TEXT NOT NULL,
            permission TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def add_user(username: str, password: str, permission: str):
    """Fügt einen Benutzer zur Datenbank hinzu."""
    try:
        conn = sqlite3.connect('databases/users.db')
        cursor = conn.cursor()

        cursor.execute('''
            INSERT INTO users (username, password, permission)
            VALUES (?, ?, ?)
        ''', (username, password, permission))

        conn.commit()
        conn.close()
        logging.info(f'Added new user: {username}')
    except sqlite3.Error as e:
        logging.error(f"Database error: {e}")

class LoginModule:
    def __init__(self):
        logging.info('Creating Login Window (TK Window)')
        self.root = tk.Tk()
        self.root.title("Login Module")
        self.root.geometry("300x200")
        self.root.resizable(False, False)

        self.username_label = tk.Label(self.root, text="Username:", font=("Arial", 12))
        self.username_label.pack(pady=10)

        self.username_entry = tk.Entry(self.root, font=("Arial", 12), width=20)
        self.username_entry.pack()

        self.password_label = tk.Label(self.root, text="Password:", font=("Arial", 12))
        self.password_label.pack(pady=10)

        self.password_entry = tk.Entry(self.root, font=("Arial", 12), width=20, show="*")
        self.password_entry.pack()

        self.login_button = tk.Button(self.root, text="Login", font=("Arial", 12), command=self.check_credentials)
        self.login_button.pack(pady=10)
        logging.info('Finished Creating Login Window')
        
        self.login: bool = False
        self.perms: str = 'user'
        logging.info(f'Set variables \'{self.login = }\' and \'{self.perms = }\'')

    def check_credentials(self):
        username = self.username_entry.get().lower().strip()
        password = self.password_entry.get().strip()
        logging.info(f'User inputted \'{username = }\' and \'password (secret)\'')
        
        try:
            conn = sqlite3.connect('databases/users.db')
            cursor = conn.cursor()

            cursor.execute('SELECT password, permission FROM users WHERE username = ?', (username,))
            user_data = cursor.fetchone()

            if user_data and user_data[0] == password:
                self.root.destroy()
                from main_functions import userset
                userset(username)
                self.login = True
                self.perms = user_data[1]
                logging.info(f'User \'{username = }\' logged in with permission \'{self.perms}\'')
                sl.success('Successfully logged in!')
            else:
                logging.warning(f"Invalid login attempt with {username} and password")
                sl.error("Invalid username or password")
                self.root.destroy()

            conn.close()

        except sqlite3.Error as e:
            logging.error(f"Database error: {e}")
            sl.error("Database error occurred")
            self.root.destroy()
        except Exception as e:
            logging.error(f'An error occurred: {e}')
            sl.error(f'An error occurred: {e}')
            self.root.destroy()

    def run(self):
        logging.info('Calling Login Window')
        self.root.mainloop()
        return self.login

def loginGui() -> list[bool, str]:
    lm = LoginModule()
    out = [lm.run(), lm.perms]
    logging.info(f'Got output from Login Window: \'{out}\'')
    return out
