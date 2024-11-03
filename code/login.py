import tkinter as tk
import logging
from SystemLogger import SystemLogger
from settings import settings

sl = SystemLogger()

logName = settings['logging']['file_login']['logFile']
logLevel = settings['logging']['file_login']['logLevel']
logFormat = settings['logging']['file_login']['logFormat']
logging.basicConfig(filename=logName, level=logLevel, format=logFormat)

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
        logging.info('Finished Creatning Login Window')
        
        self.login: bool = False
        self.perms: str = 'user'
        logging.info(f'Set variables \'{self.login = }\' and \'{self.perms = }\'')

    def check_credentials(self):
        username = self.username_entry.get().lower().strip()  # Bereinigung von Leerzeichen
        password = self.password_entry.get().strip()
        logging.info(f'User inputed \'{username = }\' and \'password (secret)\'')
        
        try:
            with open('terminal.secret', 'r') as file:
                for line in file.readlines():
                    stored_username, stored_password, stored_permission = line.strip().split(',')
                    if username == stored_username.lower() and password == stored_password:
                        self.root.destroy()
                        from main_functions import userset
                        userset(username)
                        self.login = True  # Korrektur hier
                        self.perms = stored_permission
                        logging.info(f'User \'{username = }\' logged in with permission \'{self.perms}\'')
                        sl.success('Successfully logged in!')
                        return
            
            # Falls keine Übereinstimmung gefunden wurde, ungültiger Login
            logging.warning(f"Invalid login attempt with {username} and {password}")
            sl.error("Invalid username or password")
            self.root.destroy()  # Fenster schließen bei ungültigen Daten

        except FileNotFoundError:
            print("Datei nicht gefunden")
            logging.error('Datei nicht gefunden')
            sl.error("Datei nicht gefunden")
            self.root.destroy()
        except Exception as e:
            print(f"Ein Fehler ist aufgetreten: {e}")
            logging.error(f'Ein Fehler ist aufgetreten: {e}')
            sl.error(f'Ein Fehler ist aufgetreten: {e}')
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