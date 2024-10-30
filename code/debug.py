from SystemLogger import SystemLogger
from settings import settings

SystemLogger = SystemLogger()

class debug:
    def __init__(self) -> None:
        pass

    def debugShow(self, colors: bool = False, formats: bool = False, symbols: bool = False) -> None:
        if  colors:
            print(' | '.join(f'{settings["colors"][color]}{color}\033[0m' for color in settings['colors']))
        
        if formats:
            print(' | '.join(f'{settings["formats"][format]}{format}\033[0m' for format in settings['formats']))
        
        if symbols:
            print(' | '.join(f'{settings["symbols"][symbol]} {symbol}\033[0m' for symbol in settings['symbols']))
    
    def testSystemLogger(self) -> None:
        SystemLogger.debug("This is a Debug")
        SystemLogger.info("This is an Info")
        SystemLogger.success("This is a Success")
        SystemLogger.warning("This is a Warning")
        SystemLogger.error("This is an Error")
        SystemLogger.critical("This is a Critical", -1)
    
    def size(self, draw: bool = False) -> None:
        height = settings["terminal"]["height"]
        width = settings["terminal"]["width"]
        print(f"Height: {height} | Width: {width}")
        
        if draw:
            print("*"*int(width))

            for i in range(height):
                print(i)


