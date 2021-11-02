import config
import platform


def help():
    return 'info - information about the program\nclear - clear the terminal\nexit - stop the program'

def info():
    return f'Name: {config.NAME}\nVersion: {config.VERSION}\nPython version: {platform.python_version()}\nAuthor: {config.AUTHOR}'