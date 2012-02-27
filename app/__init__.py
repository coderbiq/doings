#-*-coding:utf-8-*-
import os


def get_config():
    return Config(os.path.join(os.curdir,'app'))

class Config(object):

    def __init__(self, app_root):
        self.configs = {}
        modules = os.listdir(app_root)
        for module_name in modules:
            if os.path.isdir(module_name):
                module = __import__(module_name, globals(), locals(), ['CONFIGS'])
                self.configs.update(module.CONFIGS)

    def get(self, name):
        value_tmp = None
        for path in name.split('/'):
            if value_tmp == None:
                if(self.configs.has_key(path)):
                    value_tmp = self.configs[path]
            else:
                if(value_tmp.has_key(path)):
                    value_tmp = value_tmp[path]

        return value_tmp
