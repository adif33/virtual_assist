from plugins.APlugin import Plugin


class LightPlugin(Plugin):
    def __init__(self):
        print 1
        super(LightPlugin, self).__init__()

    def add_commands(self):
        self.add_command(self, 'lights on', self.lights_on)

    def lights_on(self):
        print 'set light on'

def main():
    from analayzer import Analyzer
    anal = Analyzer()
    LightPlugin()
    print anal.commands


if __name__ == '__main__':
    main()