import config
from assets import commands, events

def main():
    events.clear()
    print(f'{config.NAME} v{config.VERSION}')
    while True:
        cmd = input('> ')
        if cmd == 'help':
            print(commands.help())
        elif cmd == 'clear':
            events.clear()
        elif cmd == 'info':
            print(commands.info())
        elif cmd == 'exit':
            break
        else:
            print(f'Command {cmd} not found. Try help')


if __name__ == '__main__':
    main()