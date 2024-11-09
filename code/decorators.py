import time
from functools import wraps
import logging
###############################
class SystemLogger:
    def __init__(self) -> None:
        self.warningCol = '\033[93m'
        self.errorCol = '\033[91m'
        self.warningSym = '\u26A0'
        self.errorSym = '\u2717'
        self.bold = '\033[1m'
        self.blink = '\033[5m'
        self.reset = '\033[0m'
    
    def warning(self, message: str) -> None:
        print(f' {self.warningCol}{self.blink}{self.warningSym}{self.reset}{self.warningCol}  {message}{self.reset}')
    
    def error(self, message: str) -> None:
        print(f' {self.errorCol}{self.errorSym}{self.bold}  {message}{self.reset}')
###############################
last_called = {}
SystemLogger = SystemLogger()


def confirm_exit(func):
    def wrapper(*args, **kwargs):
        confirmation = SystemLogger.confirm("Are you sure you want to exit? (yes/no): ")
        if confirmation:
            return func(*args, **kwargs)
    return wrapper

def confirm(func):
    def wrapper(*args, **kwargs):
        confirmation = SystemLogger.confirm("Are you sure you want to proceed? (yes/no): ")
        if confirmation:
            return func(*args, **kwargs)
    return wrapper

def cooldown(seconds):
    def decorator(func):
        def wrapper(*args, **kwargs):
            current_time = time.time()
            last_time = last_called.get(func.__name__, 0)
            if current_time - last_time < seconds:
                SystemLogger.warning(f"Please wait {seconds - (current_time - last_time):.2f} seconds before using '{func.__name__}' again.")
                logging.warning(f"Please wait {seconds - (current_time - last_time):.2f} seconds before using '{func.__name__}' again.")
                return
            last_called[func.__name__] = current_time
            return func(*args, **kwargs)
        return wrapper
    return decorator

from functools import wraps
import logging

def deactivate(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        SystemLogger.error(f'The function "{func.__name__}" is currently deactivated!')
        logging.error(f'The function "{func.__name__}" is currently deactivated!')
        return None
    return wrapper
