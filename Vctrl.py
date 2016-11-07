
from subprocess import call
import os
import subprocess


class Verctrl:
    def __init__(self):
        pass
    def check_version(self, link, sets):
        os.chdir(sets)
        try:
            call(["rm", "-rf", "fcards-python"])
        except FileNotFoundError:
            pass
        FNUL=open(os.devnull, 'w')
        call(["git", "clone", link+".git"], stdout=FNUL, stderr=subprocess.STDOUT)
        
        cersions = open("fcards-python/VERSION", 'r')
        var = cersions.read()
        cersions.close() 
        os.chdir("..")
        return var
    def update_and_end(self, FDIR, sets):
        call(["rm", "-rf","usr/sbin/flashcards"])
        call(["cp", "-rf", sets + "/fcards-python/fcards", "/usr/sbin/flashcards"])
