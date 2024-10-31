import logging
from SystemLogger import SystemLogger
from settings import settings
from runner import runner
from main_functions import get_input

runner = runner()
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

                cmdwa = self.compile(cmd, False)

                match cmdwa[0]:
                    case 'help':
                        for attr in dir(runner.filemode):
                            if not attr.startswith('__') and not attr.startswith('_'):
                                print(f"\033[94m{attr}\033[0m")
                    
                    case 'list':
                        runner.filemode().list()
                    
                    case 'crfol':
                        runner.filemode().crfol(cmdwa[1])
                    
                    case 'delfol':
                        runner.filemode().delfol(cmdwa[1])
                    
                    case 'delete':
                        runner.filemode().delete(cmdwa[1])
                    
                    case 'read':
                        runner.filemode().read(cmdwa[1])
                    
                    case 'write':
                        runner.filemode().write(cmdwa[1],  cmdwa[2],  cmdwa[3]) #runner.filemode().write(FileName, Content, Append)
                    
                    case _:
                        logging.info(f"Unknown command: {cmd}")
                        sl.warning(f"'{cmd}' is not a valid Command")
                        sl.warning("Run 'help' to get a list of all valid Commands")

            except KeyboardInterrupt:
                logging.info('File mode was closed due to a keyboard interruption')
                sl.info('File mode was closed due to a keyboard interruption')
                break
            except Exception as e:
                logging.error(f'An error occurred while in file mode: {e} ({e.__traceback__}')
                sl.error(f'An error occurred while in file mode: {e}')


    
    def run(self, cmd: str, attr: list) -> None:
        global fileCmdCaptureErrorKill
        logging.info(f"Running command: {cmd} with attributes: {attr}")

        match cmd:
            case 'echo':
                runner.echo(' '.join(attr))
            
            case 'exit':
                runner.exit()
            
            case 'swap':
                runner.swap(attr[0])
            
            case 'me':
                runner.me()
            
            case 'wd':
                runner.wd()
            
            case 'cs':
                runner.cs()
            
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
                for attr in dir(runner):
                    if not attr.startswith('__') and not attr.startswith('_'):
                        print(f"\033[94m{attr}\033[0m")
            
            #None of These
            case _:
                logging.info(f"Unknown command: {cmd}")
                sl.warning(f"'{cmd}' is not a valid Command")
                sl.warning("Run 'help' to get a list of all valid Commands")



