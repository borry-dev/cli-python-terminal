import commands

def main():
    commands.clear()
    while True:
        cmd = input('> ')
        if cmd == 'help':
            print(commands.help())
        elif cmd == 'clear':
            commands.clear()
        elif cmd == 'info':
            print(commands.info())
        elif cmd == 'exit':
            break
        else:
            print(f'Command {cmd} not found. Try help')


if __name__ == '__main__':
    main()
