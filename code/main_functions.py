import os

def clear_screen() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')

def get_input(msg: str) -> str:
    return input(msg)

def logo(nameRaw: str, colorName: str, colorSurrounding: str, width: int, surroundKey: str = '-',) -> None:
    surround = ' ' + surroundKey*(width-2) + ' '
    name = colorSurrounding + '|' + ' ' * ((width - len(nameRaw) - 1) // 2) + colorName + nameRaw + colorSurrounding + ' ' * ((width - len(nameRaw) - 1) // 2) + '|'

    print(f'{colorSurrounding}{surround}\033[0m')
    print(f'{name}\033[0m')
    print(f'{colorSurrounding}{surround}\033[0m')

#Current User
def userinit() -> None:
    global user
    user = None

def userget() -> str:
    global user
    return user if user else os.getlogin()

def userset(userNew: str) -> None:
    global user
    user = userNew

#Current Permission
def permsinit() -> None:
    global perms
    perms = None

def permsget() -> str:
    global perms
    return perms if perms else 'user'

def permsset(permsNew: str) -> None:
    global perms
    perms = permsNew