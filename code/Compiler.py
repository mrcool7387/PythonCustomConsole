import logging
import os
import sys
from SystemLogger import SystemLogger
from settings import settings
from VarManager import VarManager
from main_functions import get_input, userget

c =  settings['colors']['primary']
sl = SystemLogger()
fileCmdCaptureErrorKill: bool = False

class compiler:
    def __init__(self):
        logName = settings['logging']['file_compiler']['logFile']
        logLevel = settings['logging']['file_compiler']['logLevel']
        logFormat = settings['logging']['file_compiler']['logFormat']
        logging.basicConfig(filename=logName, level=logLevel, format=logFormat)

    def compile(self, code: str, run: bool = True) -> list:
        logging.info('-'*15)
        logging.info(f'Compiling Raw Code Block: {code}')

        code_raw: list =  code.split(' ')
        logging.info(f"Splitted successfully from {code} to {code_raw}")

        cmd = code_raw[0]
        attr = code_raw[1:]
        logging.info("Successfully separated  command and attributes")
        logging.info(f"Command: {cmd} | Attributes: {attr}")

        if run:
            self.run(cmd, attr)
        else:
            return code_raw
    
    def file_mode(self):
        while True:
            try:
                cmd = get_input(settings['terminal']['inputCmdStyle']['filemode'])
                if cmd == 'exit':
                    break
                
                words = cmd.split()
                for id, word in enumerate(words):
                    if word.startswith('$') and word.endswith('$'):
                        value = VarManager().get(word.replace('$', ''))
                        if value:
                            words[id] = value
                cmd = ' '.join(words)

                cmdwa = self.compile(cmd, False)

                match cmdwa[0]:
                    case 'help':
                        cp = settings['colors']['primary']
                        for cmd in settings['cmdHelp']['filemode']:
                            print(f'{settings["colors"]["primary"]}{str(cmd):40}| {settings["cmdHelp"]["filemode"][cmd]}\033[0m')
                    
                    case 'list':
                        files = os.listdir()
                        for i in range(0, len(files), 4):
                            print(c + ' '.join(files[i:i+4]))
                    
                    case 'cs':
                        os.system('cls' if os.name == 'nt' else 'clear')
                    
                    case 'crfol':
                        os.mkdir(' '.join(cmdwa[1:]))
                    
                    case 'delfol':
                        os.rmdir(' '.join(cmdwa[1:]))
                    
                    case 'delete':
                        os.remove(' '.join(cmdwa[1:]))
                    
                    case 'read':
                        with open(cmdwa[1], 'r') as file:
                            content = file.read()
                            file.close()
                            print(c + content)
                    
                    case 'write':
                        fileName = cmdwa[1]
                        txt = ' '.join(cmdwa[3:])
                        if cmdwa[2]:
                            with open(fileName, 'a') as file:
                                file.write(txt)
                        else:
                            with open(fileName, 'w') as file:
                                file.write(txt)
                        file.close()
                    
                    case _:
                        logging.info(f"Unknown command: {cmd}")
                        sl.warning(f"'{cmd}' is not a valid Command")
                        sl.warning("Run 'help' to get a list of all valid Commands")

            except KeyboardInterrupt:
                logging.info('File mode was closed due to a keyboard interruption')
                sl.info('File mode was closed due to a keyboard interruption')
                break
            except Exception as e:
                logging.error(f'An error occurred while in file mode: {e} ({e.__traceback__})')
                sl.error(f'An error occurred while in file mode: {e}')
    
    def var_mode(self):
        while True:
            try:
                cmd = get_input(settings['terminal']['inputCmdStyle']['varmode'])
                if cmd == 'exit':
                    break
                
                words = cmd.split()
                for id, word in enumerate(words):
                    if word.startswith('$') and word.endswith('$'):
                        value = VarManager().get(word.replace('$', ''))
                        if value:
                            words[id] = value
                cmd = ' '.join(words)
                
                cmdwa = self.compile(cmd, False)

                match cmdwa[0]:
                    case 'help':
                        cp = settings['colors']['primary']
                        for cmd in settings['cmdHelp']['varmode']:
                            print(f'{settings["colors"]["primary"]}{str(cmd):20}| {settings["cmdHelp"]["varmode"][cmd]}\033[0m')
                    case 'create':
                        VarManager().create(cmdwa[1])
                    
                    case 'set':
                        VarManager().set(cmdwa[1], cmdwa[2])
                    
                    case 'delete':
                        VarManager().delete(cmdwa[1])
                    
                    case 'list':
                        VarManager().list()
                    
                    case 'cs':
                        os.system('cls' if os.name == 'nt' else 'clear')
                    
                    case _:
                        logging.info(f"Unknown command: {cmd}")
                        sl.warning(f"'{cmd}' is not a valid Command")
                        sl.warning("Run 'help' to get a list of all valid Commands")

            except KeyboardInterrupt:
                logging.info('File mode was closed due to a keyboard interruption')
                sl.info('File mode was closed due to a keyboard interruption')
                break
            except Exception as e:
                logging.error(f'An error occurred while in variable mode: {e} ({e.__traceback__})')
                sl.error(f'An error occurred while in variable mode: {e}')


    
    def run(self, cmd: str, attr: list) -> None:
        global fileCmdCaptureErrorKill
        logging.info(f"Running command: {cmd} with attributes: {attr}")

        match cmd:
            case 'echo':
                print(c + ' '.join(attr))
            
            case 'exit':
                sys.exit()
            
            case 'swap':
                os.chdir(attr[0:])
            
            case 'me':
                print(c + userget())
            
            case 'wd':
                print(c + os.getcwd())
            
            case 'cs':
                os.system('cls' if os.name == 'nt' else 'clear')
            
            case 'file':
                if not fileCmdCaptureErrorKill:
                    logging.error('File Command wasn\'t captured')
                    sl.error('This Command should be captured')
                    sl.error('by \'main.py\' and set into special')
                    sl.error('mode. Please rerun this Command')
                    sl.error('If this error shows up again, please')
                    sl.error('restart the Console. If this doesn\'t')
                    sl.error('work, please contact the Developer')
                    fileCmdCaptureErrorKill = True

                else:
                    logging.critical('File Command retired an still wasn\'t captured')
                    logging.info('Stopping Console')
                    sl.error('This Command still wasn\'t captured')
                    sl.error('The Console will now be terminated.')
                    sl.error('If this problem persists, please')
                    sl.critical('contact the Developer.', 200)
            
            case 'help':
                cp = settings['colors']['primary']
                for cmd in settings['cmdHelp']['normal']:
                    print(f'{settings["colors"]["primary"]}{str(cmd):12}| {settings["cmdHelp"]["normal"][cmd]}\033[0m')
            
            #None of These
            case _:
                logging.info(f"Unknown command: {cmd}")
                sl.warning(f"'{cmd}' is not a valid Command")
                sl.warning("Run 'help' to get a list of all valid Commands")



