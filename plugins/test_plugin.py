import re

from command import Command
from plugins.base_plugin import Plugin


class TestPlugin(Plugin):
    def __init__(self):
        super(TestPlugin, self).__init__()

    def init_commands(self):
        return [Command(re.compile("do you understand me"), self.test)]

    def test(self, command_text):
        print 1