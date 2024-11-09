import logging
import os

from Compiler import compiler
from settings import settings
from debug import debug
from SystemLogger import SystemLogger
from VarManager import VarManager
from main_functions import clear_screen, logo, get_input, userget, userinit, permsinit, permsget, permsset, exsit_path
from login import loginGui, create_db, add_user

logName = settings['logging']['file_main']['logFile']
logLevel = settings['logging']['file_main']['logLevel']
logFormat = settings['logging']['file_main']['logFormat']

logging.basicConfig(filename=logName, level=logLevel, format=logFormat)
logging.info("Compiler Initialized")

SystemLogger = SystemLogger()
debug = debug()


def main():
    if not exsit_path('databases/users.db'):
        logging.warning('Database for Users do not exsists! Creating new one')
        create_db()
        add_user('admin', 'admin', 'admin')
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
    permsset(perms or permsget())


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
            
            words = cmd.split()
            for id, word in enumerate(words):
                if word.startswith('$') and word.endswith('$'):
                    value = VarManager().get(word.replace('$', ''))
                    if value:
                        words[id] = value
            cmd = ' '.join(words)
            
            if cmd == 'file':
                if 'file' in permsget() or permsget() == 'admin':
                    SystemLogger.info('Entering File Mode')
                    compiler().file_mode()
                    SystemLogger.info('Exiting File Mode')
                else:
                    SystemLogger.error('You dont have the Permission to accsess file managing mode')
                    logging.error('Denied "File" command due of permissions')
            elif cmd == 'vars':
                if 'var' in permsget() or permsget() == 'admin':
                    SystemLogger.info('Entering Variable Editor')
                    compiler().var_mode()
                    SystemLogger.info('Exiting File Mode')
                else:
                    SystemLogger.error('You dont have the Permission to manage Variables')
                    logging.error('Denied "Vars" command due of permissions')
            if cmd not in ['file', 'vars']:
                if'user' in permsget():
                    compiler().compile(cmd)
                else:
                    SystemLogger.error('You dont have the Permission to execute this command ("Vars" or "File" only)')
                    logging.error('Denied Command due of permissions ("Vars" or "File" only)')
        except KeyboardInterrupt:
            SystemLogger.info('Stopping Console due Keyboard Interrupt')
            logging.info('Compiler interrupted')
            break
        except Exception as e:
            logging.error(f'Error: {e}')

main()
input(' ')

