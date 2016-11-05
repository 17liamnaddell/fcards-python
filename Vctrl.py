
from subprocess import call
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
        call(["git", "clone", link+".git"])
        cersions = open("fcards-python/VERSION", 'r')
        var = cersions.read()
        cersions.close() 
        os.chdir("..")
        return var
    def update_and_end(self, FDIR, sets):
        call(["rm", "-rf", FDIR+"/flashcards"])
        call(["cp", "-rf", sets + "/fcards-python/fcards", FDIR + "/flashcards"])
