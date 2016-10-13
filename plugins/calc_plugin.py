import re
import redis

from command import Command
from plugins.base_plugin import Plugin


class TestPlugin(Plugin):
    def __init__(self):
        self.redis_connection = redis.Redis()
        super(TestPlugin, self).__init__()

    def init_commands(self):
        return [Command(re.compile("how much is"), self.calc_percentage)]

    def calc_percentage(self, command_text):
        result = re.findall("(\d+)\% out of (\d+)", command_text)
        if result:
            result = result[0]
            self.redis_connection.publish("voice_commands", "result:%s" % int(int(result[0])/100.0*float(result[1])))