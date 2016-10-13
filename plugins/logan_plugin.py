import re
import os

from command import Command
from plugins.base_plugin import Plugin


class LoganPlugin(Plugin):
    def __init__(self):
        super(LoganPlugin, self).__init__()

    def init_commands(self):
        return [Command(re.compile("(?:hey)|(?:hello) logan", re.I), self.say_hello),
                Command(re.compile("good morning logan", re.I), self.good_morning),
                Command(re.compile("how are you logan", re.I), self.how_are_you),
                Command(re.compile("result:", re.I), self.answer_result)]

    def say_hello(self, command_text):
        os.system("espeak 'Hello masters'")

    def good_morning(self, command_text):
        os.system("espeak 'Good morning to you too'")

    def how_are_you(self, command_text):
        os.system("espeak 'I am fine, thanks.'")

    def answer_result(self, command_text):
        os.system("espeak '%s'" % command_text.split("result:")[-1])
