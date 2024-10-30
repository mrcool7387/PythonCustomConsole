from datetime import datetime
import os

width, height = os.get_terminal_size()
wd, user = os.getcwd(), os.getlogin()

settings: dict = {
    "terminal": {
        "name": "TCS-Terminal",
        "height": int(height),
        "width": int(width),
        "inputCmdStyle": {
            "normal": f"\033[92m\033[1m{wd} \033[0m\033[90m| {datetime.now().strftime('%d-%m-%Y %H.%M.%S')} | {user} \033[94m$ \033[0m",
            "filemode": f"\033[92m\033[1m{wd} \033[0m\033[90m| {datetime.now().strftime('%d-%m-%Y %H.%M.%S')} | {user} \033[94mFileMode $ \033[0m"
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
        "file_compiler": {
            "logLevel":  "DEBUG",
            "logFormat": "%(asctime)s - %(levelname)s | %(message)s",
            "logFile": f"logs/tcs-compiler-{datetime.now().strftime('%d-%m-%Y....%H.%M.%S')}.log"
        }
    }
}