import os
import sys
from settings import settings
c =  settings['colors']['primary']

class runner:
    def __init__(self):
        pass

    def cs(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def wd(self):
        print(c + os.getcwd())
    
    def me(self):
        print(c + os.getlogin())
    
    def swap(self, fol: str):
        os.chdir(fol)
    
    def echo(self, msg: str):
        print(c + msg)
    
    def exit(self):
        sys.exit()

    class filemode:
        def __init__(self):
            pass

        def list(self):
            print(c + os.listdir())
        
        def crfol(self, folName: str):
            os.mkdir(folName)
        
        def delfol(self, folName: str):
            os.rmdir(folName)
        
        def delete(self, fileName: str):
            os.remove(fileName)
        
        def write(self, fileName: str, txt: str, append: bool = False):
            if append:
                with open(fileName, 'a') as file:
                    file.write(txt)
            else:
                with open(fileName, 'w') as file:
                    file.write(txt)
            file.close()
        
        def read(self, fileName: str):
            with open(fileName, 'r') as file:
                content = file.read()
                file.close()
                print(c + content)