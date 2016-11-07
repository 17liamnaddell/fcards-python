
from subprocess import call
import subprocess
import os



class Verctrl:
    def __init__(self):
        pass
    def check_version(self, link, sets):
        os.chdir(sets)
        try:
            call(["rm", "-rf", "fcards-python"])
        except FileNotFoundError:
            pass
        FNULL=open(os.devnull, 'w')
        call(["git", "clone", link+".git"], stdout=FNULL, stderr=subprocess.stdout)
        cersions = open("fcards-python/VERSION", 'r')
        var = cersions.read()
        cersions.close() 
        os.chdir("..")
        return var
    def update_and_end(self, FDIR, sets):
        call(["rm", "-f", "usr/sbin/flashcards"])
        call(["cp", "-rf", sets + "/fcards-python/fcards", FDIR + "/flashcards"])
