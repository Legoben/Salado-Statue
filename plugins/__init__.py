import os

__all__ = []

path = os.path.abspath('plugins')

for plugin in os.listdir(path):
    if plugin[-3:] == '.py':
        if plugin[:-3] != '__init__':
            __all__.append(plugin[:-3])




