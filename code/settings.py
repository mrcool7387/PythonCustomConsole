from datetime import datetime
from main_functions import userget, userinit, init
import os

width, height = os.get_terminal_size()
wd = os.getcwd()
init()

settings: dict = {
    "terminal": {
        "name": "TCS-Terminal",
        "login": True,
        "height": int(height),
        "width": int(width),
        "me": f"{userinit()}{userget()}",
        "inputCmdStyle": {
            "normal": f"\033[92m\033[1m{wd} \033[0m\033[90m| {datetime.now().strftime('%d-%m-%Y %H.%M.%S')} | {userget()} \033[94m$ \033[0m",
            "filemode": f"\033[92m\033[1m{wd} \033[0m\033[90m| {datetime.now().strftime('%d-%m-%Y %H.%M.%S')} | {userget()} \033[94mFileMode $ \033[0m",
            "varmode": f"\033[92m\033[1m{wd} \033[0m\033[90m| {datetime.now().strftime('%d-%m-%Y %H.%M.%S')} | {userget()} \033[94mVariableMode $ \033[0m"
        }
    },
    "colors": {
        "primary": "\033[94m",
        "secondary": "\033[90m",
        "success": "\033[92m",
        "error": "\033[91m",
        "warning": "\033[93m",
        "info": "\033[96m",
        "debug": "\033[95m",
        "question": "\033[95m",
        "light": "\033[97m",
        "dark": "\033[90m"
    },
    "formats": {
        "bold": "\033[1m",
        "underline": "\033[4m",
        "italic": "\033[3m",
        "reset": "\033[0m",
        "blinking": "\033[5m",
        "reverse": "\033[7m",
        "hidden": "\033[8m",
        "strikethrough": "\033[9m",
        "doubleunderline": "\033[21m",
        "framed": "\033[51m",
        "encircled": "\033[52m",
        "overlined": "\033[53m"
    },
    "symbols": {
        "check": "\u2713",
        "cross": "\u2717",
        "info": "\u2139",
        "warning": "\u26A0",
        "question": "\u2753",
        "debug": "\u2699"
    },
    "logging": {
        "file_login": {
            "logLevel":  "INFO",
            "logFormat": "%(asctime)s - %(levelname)s | %(message)s",
            "logFile": f"logs/tcs-login-{datetime.now().strftime('%d-%m-%Y....%H.%M.%S')}.log"
        },
        "file_systemlogger": {
            "logLevel":  "DEBUG",
            "logFormat": "%(asctime)s - %(levelname)s | %(message)s",
            "logFile": f"logs/tcs-systemlogger-{datetime.now().strftime('%d-%m-%Y....%H.%M.%S')}.log"
        },
        "file_main": {
            "logLevel":  "INFO",
            "logFormat": "%(asctime)s - %(levelname)s | %(message)s",
            "logFile": f"logs/tcs-main-{datetime.now().strftime('%d-%m-%Y....%H.%M.%S')}.log"
        },
        "file_varmgr": {
            "logLevel":  "INFO",
            "logFormat": "%(asctime)s - %(levelname)s | %(message)s",
            "logFile": f"logs/tcs-varmgr-{datetime.now().strftime('%d-%m-%Y....%H.%M.%S')}.log"
        },
        "file_compiler": {
            "logLevel":  "DEBUG",
            "logFormat": "%(asctime)s - %(levelname)s | %(message)s",
            "logFile": f"logs/tcs-compiler-{datetime.now().strftime('%d-%m-%Y....%H.%M.%S')}.log"
        }
    },
    "cmdHelp": {
        "normal": {
            "help": "Displays This List",
            "exit": "Exits The Program",
            "cs": "Clears The Screen",
            "wd": "Displays the current WorkDictonary",
            "swap [path]":  "Changes the WorkDictonary",
            "me": "Displays the current User",
            "echo [msg]":  "Echoes the input"
        },
        "filemode": {
            "help": "Displays This List",
            "exit": "Exits The Program",
            "cs": "Clears The Screen",
            "list": "Lists the files in the current directory",
            "crfol [folName]": "Creates a new folder",
            "delfol [folName]": "Deletes a folder",
            "delete [fileName]": "Delets a file",
            "write [fileName] [content] [True:False]": "Writes to a file",
            "read [fileName]": "Reads from a file"
        },
        "varmode": {
            "help": "Displays This List",
            "exit": "Exits The Program",
            "cs": "Clears The Screen",
            "list": "Lists the variables in the current instance",
            "new [name]": "Creates a new variable",
            "set [name] [value]": "Sets the value of a variable",
            "delete [name]": "Delete a Variable?"
        }
    }
}