#-*-coding:utf-8-*-
import os


def get_config():
    return Config(os.path.join(os.curdir,'app'))

class Config(object):

    def __init__(self, app_root):
        self.configs = {'modules':{}, 'routers':[]}
        self.app_root = app_root
        self._load_config()

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

    def _load_config(self):
        modules = os.listdir(self.app_root)
        for module_name in modules:
            if self._is_module(module_name):
                module = __import__(module_name, globals(), locals(), ['CONFIGS'])
                self._extends_config(module.CONFIGS, module_name)

    def _is_module(self, module_name):
        is_module = True
        module_path = os.path.join(self.app_root, 
                                    module_name)
        if not os.path.isdir(module_path):
            is_module = False
        return is_module

    def _extends_config(self, configs, module_name):
        if configs.has_key('module'):
            self.configs['modules'][module_name] = configs['module']
            del configs['module']
        if configs.has_key('routers'):
            self.configs['routers'].extend(configs['routers'])
        if configs.has_key(module_name):
            self.configs[module_name] = configs[module_name]
