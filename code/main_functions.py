import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_input(msg: str) -> str:
    return input(msg)

def logo(nameRaw: str, colorName: str, colorSurrounding: str, width: int, surroundKey: str = '-',) -> None:
    surround = ' ' + surroundKey*(width-2) + ' '
    name = colorSurrounding + '|' + ' ' * ((width - len(nameRaw) - 1) // 2) + colorName + nameRaw + colorSurrounding + ' ' * ((width - len(nameRaw) - 1) // 2) + '|'

    print(f'{colorSurrounding}{surround}\033[0m')
    print(f'{name}\033[0m')
    print(f'{colorSurrounding}{surround}\033[0m')
