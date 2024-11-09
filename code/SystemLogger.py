from settings import settings
import sys

class SystemLogger:
    def __init__(self) -> None:
        # Logging Settings
        self.logLevel = settings['logging']['file_systemlogger']['logLevel']
        self.LogFile = settings['logging']['file_systemlogger']['logFile']
        self.logFormat = settings['logging']['file_systemlogger']['logFormat']

        # Colors
        self.infoCol = settings['colors']['info']
        self.warningCol = settings['colors']['warning']
        self.errorCol = settings['colors']['error']
        self.successCol = settings['colors']['success']
        self.debugCol = settings['colors']['debug']
        self.questionCol = settings['colors']['question']

        # Symbols
        self.infoSym = settings['symbols']['info']
        self.warningSym = settings['symbols']['warning']
        self.errorSym = settings['symbols']['cross']
        self.successSym = settings['symbols']['check']
        self.debugSym = settings['symbols']['debug']
        self.questionSym = settings['symbols']['question']

        #Formats
        self.bold = settings['formats']['bold']
        self.italic = settings['formats']['italic']
        self.blink = settings['formats']['blinking']
        self.reset = settings['formats']['reset']
    
    def debug(self, message: str) -> None:
        print(f' {self.debugCol}{self.debugSym}{self.italic}  {message}{self.reset}')
    
    def info(self, message: str) -> None:
        print(f' {self.infoCol}{self.infoSym}  {message}{self.reset}')
    
    def confirm(self, message: str) -> bool:
        ans = input(f' {self.questionCol}{self.questionSym}  {message}{self.reset}')
        if ans.lower() in ['y', 'yes', 'j', 'ja']:
            return True
        elif ans.lower() in ['n', 'no', 'nein']:
            return False
        else:
            self.warning(f'"{ans}" is not a Answer for a yes/no question!')
            return self.confirm(message)
    def success(self, message: str) -> None:
        print(f' {self.successCol}{self.successSym}  {message}{self.reset}')
    
    def warning(self, message: str) -> None:
        print(f' {self.warningCol}{self.blink}{self.warningSym}{self.reset}{self.warningCol}  {message}{self.reset}')
    
    def error(self, message: str) -> None:
        print(f' {self.errorCol}{self.errorSym}{self.bold}  {message}{self.reset}')
    
    def critical(self, message: str, errorCode: int) -> None:
        self.error(message)
        print(f'\n {self.errorCol}{self.italic}Program exited with Code {errorCode}{self.reset}')
        sys.exit()