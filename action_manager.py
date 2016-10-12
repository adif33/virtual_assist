from plugins.APlugin import Plugin


def get_command():
    return 'dimm light'


def analyzer(command):
    return Plugin()

def action_manager():
    while True:
        command = get_command()
        plugin = analyzer(command)

        # will return plugin name, reference or instance?
        plugin.execute(command)

        break


def main():
    action_manager()

if __name__ == '__main__':
    main()