from singeltone import Singleton
import cPickle as pickle


class Analyzer(object):
    __metaclass__ = Singleton

    def __init__(self):
        self.command_patterns = list()

    def add_command_to_redis(self, command):
        self.command_patterns.append(command)

    def command_to_action(self, command_text):
        identified = False
        for command_obj in self.command_patterns:
            if command_obj.re_command.search(command_text):
                identified = True
                command_obj.activate(command_text)
                print "Great Success on command: {command_text} of command_action: {action}"\
                      .format(command_text=command_text, action=command_obj.action.__name__)

        if not identified:
            print "was unable to identify the command: %s" % command_text
