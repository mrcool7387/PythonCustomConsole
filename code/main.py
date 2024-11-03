import logging
from random import *

from Compiler import compiler
from settings import settings
from debug import debug
from SystemLogger import SystemLogger
from main_functions import clear_screen, logo, get_input, userset, userget, userinit, permsinit, permsget, permsset
from login import loginGui

logName = settings['logging']['file_main']['logFile']
logLevel = settings['logging']['file_main']['logLevel']
logFormat = settings['logging']['file_main']['logFormat']

logging.basicConfig(filename=logName, level=logLevel, format=logFormat)
logging.info("Compiler Initialized")

SystemLogger = SystemLogger()
debug = debug()

def main():
    clear_screen()
    userinit()
    permsinit()
    
    logo(settings['terminal']['name'], '\033[92m', '\033[90m', settings['terminal']['width'])
    
    login, perms = None, None
    if settings['terminal']['login']:
        login, perms = loginGui()
        if not login:
            logging.critical('Wrong Username or Password')
            SystemLogger.critical('Wrong Username or Passwort', 205)
    else:
        SystemLogger.warning('Login is disabled')
        logging.warning('Login is disabled')
    permsset(perms if perms else permsget())
        

    SystemLogger.info(f'Welcome {userget().capitalize()} to {settings["terminal"]["name"]}')
    SystemLogger.info(f'Your current Permission is \'{permsget()}\'')
    SystemLogger.info('Run the Command "help" to get a List')
    SystemLogger.info('of all Commands')
    print(' ')
    if  permsget() == 'admin':
        SystemLogger.warning('You are an Admin, be careful!')
        print(' ')
    
    while True:
        try:
            cmd = get_input(settings['terminal']['inputCmdStyle']['normal'])
            if cmd == 'file':
                SystemLogger.info('Entering File Mode')
                compiler().file_mode()
                SystemLogger.info('Exiting File Mode')
            if cmd != 'file':
                compiler().compile(cmd)
        except KeyboardInterrupt:
            SystemLogger.info('Stopping Console due Keyboard Interrupt')
            logging.info('Compiler interrupted')
            break
        except Exception as e:
            logging.error(f'Error: {e}')



main()
    

