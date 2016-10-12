import redis
from glob import glob

from analayzer import Analyzer
from utils.import_utils import converting_file_path_to_import_path, import_by_path, PLUGINS_PATH_PATTERN

analyzer = Analyzer()
redis_connection = redis.Redis()
pubsub = redis_connection.pubsub()
pubsub.subscribe("voice_commands")


def get_command():
    for message in pubsub.listen():
        if message["type"] == "message":
            yield message["data"]


def analyze(command_text):
    return analyzer.command_to_action(command_text)


def init_plugins():
    files = glob(PLUGINS_PATH_PATTERN)
    for file_path in files:
        converted_path = converting_file_path_to_import_path(file_path)
        if converted_path:
            import_file_path, class_name = converted_path
            mod = import_by_path(import_file_path, class_name)
            plugin_class = getattr(mod, class_name)
            plugin_class()


def action_manager():
    for voice_command in get_command():
        analyze(voice_command)


def main():
    init_plugins()
    action_manager()

if __name__ == '__main__':
    main()
