import os
import config


def clear():
    os.system('clear||cls')

def help():
    return 'info - information about the program\nclear - clear the terminal\nexit - stop the program'

def info():
    return f'Version: {config.VERSION}\nAuthor: {config.AUTHOR}'