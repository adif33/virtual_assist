from singeltone import Singleton

class Analyzer(object):
    __metaclass__ = Singleton

    def __init__(self):
        # redis
        self.commands = []  # TODO: is list the best????

    def add_command_to_queue(self, command):
        self.commands.append(command)
