import os

def clear_screen() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')

def get_input(msg: str) -> str:
    return input(msg)

def logo(nameRaw: str, colorName: str, colorSurrounding: str, width: int, surroundKey: str = '-') -> None:
    surround = ' ' + surroundKey * (width - 2) + ' '
    name = (
        f'{colorSurrounding}|'
        + ' ' * ((width - len(nameRaw) - 1) // 2)
        + colorName
        + nameRaw
        + colorSurrounding
        + ' ' * ((width - len(nameRaw) - 1) // 2)
        + '|'
    )

    print(f'{colorSurrounding}{surround}\033[0m')
    print(f'{name}\033[0m')
    print(f'{colorSurrounding}{surround}\033[0m')

def exsit_path(path: str) -> bool:
    return os.path.exists(path)

# Initialize global variables
userInitHappen: bool = True
permsInitHappen: bool = True
user = ''
perms = ''

def init() -> None:
    global userInitHappen, permsInitHappen
    userInitHappen = True
    permsInitHappen = True

def userinit() -> None:
    global user, userInitHappen
    if userInitHappen:
        user = userget() or ''
        userInitHappen = False

def userget() -> str:
    global user
    try:
        return user
    except Exception:
        return os.getlogin()

def userset(userNew: str) -> None:
    global user
    user = userNew

# Current Permission

def permsinit() -> None:
    global perms, permsInitHappen
    if permsInitHappen:
        perms = permsget() or ''
        permsInitHappen = False

def permsget() -> str:
    global perms
    try:
        return perms
    except Exception:
        return 'user'

def permsset(permsNew: str) -> None:
    global perms
    perms = permsNew