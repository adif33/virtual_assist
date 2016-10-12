from analayzer import Analyzer

class Plugin(object):
    def __init__(self):
        print 2
        self.commands = []
        self.register_plugin()

    def register(self):
        self.register_plugin()

    def register_plugin(self):
        self.add_commands()
        for command in self.commands:
            print 'here: ', command
            Analyzer.add_command_to_queue(command)


    def add_command(self,  re_command, action, timeout=0):
        # TODO: why not to the analyzr??
        self.commands.append(Command(self,  re_command, action, timeout))

    def add_commands(self):
        raise NotImplementedError

    def execute(self, action):
        print "Do %s" % action


class Command(object):
    def __init__(self, father_plugin, re_command, action, timeout=0):
        # self.father_plugin = father_plugin
        # TODO: why not delete itself?
        self.re_command = re_command
        self.action = action
        self.timeout = timeout
        self.lifetime = None
        self.start_counting_time()  # TODO: why it counts the time? and not from outside

    def start_counting_time(self):
        pass

    def is_dead(self):
        if not self.lifetime:
            self.start_counting_time()
        return False

    def is_suited(self, command):
        if self.is_dead():
            return False

        return True  # TODO

    def activate(self, command):
        self.action(command)
