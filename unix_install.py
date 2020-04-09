import sys, traceback
import subprocess
import importlib, site

class InstallerClass:
    msgpy = ['python3', '-m', 'pip', 'uninstall', 'msgpack-python']
    #msg = ['python', '-m', 'pip', 'install', '-U' ,'msgpack']
    msg = ['python3', '-m', 'pip', 'install', 'msgpack==1.0.0']
    nump = ['python3', '-m', 'pip', 'install', 'numpy']
    pyn = ['python3', '-m', 'pip', 'install', 'pynvim']
    pan = ['python3', '-m', 'pip', 'install', 'pandas']

    def msgpy_method(self):
        try:
            ret_msgpy = subprocess.run(self.msgpy, encoding='utf-8', stderr=subprocess.PIPE)
            print(ret_msgpy)
        except Exception:
            traceback.print_exc()
    def msg_method(self):
        try:
            ret_msg = subprocess.run(self.msg, encoding='utf-8', stderr=subprocess.PIPE)
            print(ret_msg)
        except Exception:
            traceback.print_exc()
    def nump_method(self):
        try:
            ret_nump = subprocess.run(self.nump, encoding='utf-8', stderr=subprocess.PIPE)
            print(ret_nump)
        except Exception:
            traceback.print_exc()
    def pyn_method(self):
        try:
            ret_pyn = subprocess.run(self.pyn, encoding='utf-8', stderr=subprocess.PIPE)
            print(ret_pyn)
        except Exception:
            traceback.print_exc()
    def pan_method(self):
        try:
            ret_pan = subprocess.run(self.pan, encoding='utf-8', stderr=subprocess.PIPE)
            print(ret_pan)
        except Exception:
            traceback.print_exc()

InstClass = InstallerClass()
InstClass.msgpy_method()
InstClass.msg_method()
InstClass.nump_method()
InstClass.pyn_method()
InstClass.pan_method()

importlib.reload(site)
