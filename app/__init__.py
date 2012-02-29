#-*-coding:utf-8-*-
import os


def get_config():
    return Config(os.path.join(os.curdir,'app'))


class Config(object):
    """配置类搜索app根目录下的所有子模块从中加载CONFIGS字典\n
        并将所有模块CONFIGS字典合并到一个字典中\n
        供应用程序调用各种配置信息"""
    def __init__(self, app_root=None):
        self.configs = {}
        self.app_root = app_root
        self._load_config()

    def get(self, name):
        """获取指定字典路径下的配置项，如果没有找到相关配置则返回None"""
        value = self.configs;
        for path in name.split('/'):
            if(value.has_key(path)):
                value = value[path]
            else:
                return None
        return value

    def extends(self, configs, target = None):
        if target == None:
            target = self.configs
        for (key, value) in configs.items():
            if not target.has_key(key):
                target[key] = value
            elif type(value) != dict:                
                if type(value) == list and type(target[key]) == list:
                    target[key].extend(value)
                else:
                    target[key] = value
            else:
                target[key] = self.extends(value, target[key])
        return target

    def _load_config(self):
        modules = open(os.path.join(self.app_root, 'modules'))
        try:
            for module_name in modules:
                module = __import__(module_name, globals(), locals(), 
                                    ['CONFIGS'])
                self.extends(module.CONFIGS)
        finally:
            modules.close()

    def _is_module(self, module_name):
        is_module = True
        module_path = os.path.join(self.app_root, module_name)
        if not os.path.isdir(module_path):
            is_module = False
        return is_module

if __name__ == '__main__':
    modules = open('./modules')
    try:
        for module_name in modules.readlines():
            path = os.path.join(os.curdir, module_name)
            print type(path)
            print os.path.isdir(path)
            print '\n'
    finally:
        modules.close()
