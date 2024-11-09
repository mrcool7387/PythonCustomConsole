import logging

from SystemLogger import SystemLogger
from settings import settings
from decorators import confirm

logName = settings['logging']['file_varmgr']['logFile']
logLevel = settings['logging']['file_varmgr']['logLevel']
logFormat = settings['logging']['file_varmgr']['logFormat']
logging.basicConfig(filename=logName, level=logLevel, format=logFormat)

sl = SystemLogger()

##########################
# The Variable Dictonary #
##########################

vars: dict = {'Sample': 'A sample Variable'}

##########################

class VarManager:
    def __init__(self):
        pass
    
    def create(self, varName: str) -> None:
        logging.info(f'Sending Request to create Variable "{varName}"')
        if not varName in vars:
            vars[varName] = None
            logging.info(f'Variable "{varName}" created with value None')
            sl.info(f'Variable "{varName}" created with value None')
        else:
            logging.warning(f'Variable "{varName}" already exists')
            sl.warning(f'Variable {varName} already exists')
    
    @confirm
    def delete(self, varName: str) -> None:
        logging.info(f'Sending Request to delete Variable "{varName}"')
        if varName in vars:
            name, value = varName, vars[varName]
            del vars[varName]
            logging.info(f'Variable {name} deleted with last value {value}')
            sl.info(f'Variable {name} deleted with last value {value}')
        else:
            logging.warning(f'Variable "{varName}" does not exist')
            sl.warning(f'Variable {varName} does not exist')
    
    def set(self, varName: str, value) -> None:
        logging.info(f'Sending Request to set Variable "{varName}" to {value}')
        if varName in vars:
            name, old, new = varName, vars[varName], value
            vars[varName] = new
            logging.info(f'Set Variable {name} to {new} (OLD: {old})')
            sl.info(f'Set Variable {name} to {new} (OLD: {old})')
        else:
            logging.warning(f'Variable "{varName}" does not exist')
            sl.warning(f'Variable {varName} does not exist')
    
    def get(self, varName: str):
        logging.info(f'Sending Request to get Variable "{varName}"')
        if varName in vars:
            sl.info(f'Variable {varName} has value {vars[varName]}')
            return vars[varName]
        else:
            logging.warning(f'Variable "{varName}" does not exist')
            sl.warning(f'Variable {varName} does not exist')
            return None
    
    def list(self) -> None:
        logging.info(f'Sending Request to list all Variables')
        for name, value in vars.items():
            logging.info(f'Variable {name} has value {value}')
            sl.info(f'Variable "{name}" has value: {value}')


class VariableError(Exception):
    def __init__(self, message: str) -> None:
        sl.error(message)
        logging.error(message)
        self.message = message
        super().__init__(self.message)