import pip, site, importlib

pip.main(['uninstall', 'msgpack-python'])
#pip.main(['install','msgpack'])
pip.main(['install','-U','msgpack'])
pip.main(['install','numpy'])
pip.main(['install','pynvim'])

importlib.reload(site)
