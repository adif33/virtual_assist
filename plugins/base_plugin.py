from analayzer import Analyzer


class Plugin(object):
    def __init__(self):
        self.analyzer = Analyzer()
        self.commands = self.init_commands()
        self.register_plugin()

    def register_plugin(self):
        self.add_commands()

    def init_commands(self):
        raise NotImplementedError

    def add_command_to_analyzer(self, command):
        self.analyzer.add_command_to_redis(command)

    def add_commands(self):
        for command in self.commands:
            self.add_command_to_analyzer(command)
