import re

plugin_heritage_re = re.compile("class (.*?)\(Plugin\)")
PLUGINS_PATH_PATTERN = "plugins/*.py"


def converting_file_path_to_import_path(file_path):
    f = open(file_path)
    re_result = plugin_heritage_re.findall(f.read())
    if re_result:
        class_name = re_result[0]
        import_file_path = ".".join(file_path.replace("/", ".").split(".")[:-1])
        return import_file_path, class_name


def import_by_path(import_file_path, class_name):
    return __import__(import_file_path, fromlist=[class_name])
