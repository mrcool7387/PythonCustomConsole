import logging
import os
import random
from random import *
import datetime

from Compiler import compiler
from settings import settings
from debug import debug
from SystemLogger import SystemLogger
from main_functions import clear_screen, logo, get_input

logName = settings['logging']['file_main']['logFile']
logLevel = settings['logging']['file_main']['logLevel']
logFormat = settings['logging']['file_main']['logFormat']

logging.basicConfig(filename=logName, level=logLevel, format=logFormat)
logging.info("Compiler Initialized")

SystemLogger = SystemLogger()
debug = debug()

def main():
    clear_screen()
    logo(settings['terminal']['name'], '\033[92m', '\033[90m', settings['terminal']['width'])

    SystemLogger.info(f'Welcome {os.getlogin()} to {settings["terminal"]["name"]}')
    SystemLogger.info('Run the Command "help" to get a List')
    SystemLogger.info('of all Commands')
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

if __name__ == '__main__':
    main()
    
    

