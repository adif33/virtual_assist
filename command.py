class Command(object):
    def __init__(self, re_command, action, timeout=0):
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

    def is_alive(self, command):
        if self.is_dead():
            return False

        return True  # TODO

    def activate(self, command_text):
        return self.action(command_text)
