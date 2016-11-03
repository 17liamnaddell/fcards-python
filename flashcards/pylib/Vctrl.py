
from subprocess import call
import os
class Vctrl:
    def __init__(self):
        self.myValue = "bananna"
    def check_version(self, link, sets):
        os.getcwd()
        os.chdir(sets)
        try:
            call(["rm", "-rf", "fcards"])
        except FileNotFoundError:
            pass
        call(["git", "clone", link+".git"])
        cersions = open("fcards/VERSION")
        os.chdir("..")
        print(cersions.read())
        self.myValue = cersions.read()
        return self.myValue
        #try:
        #    os.chdir(sets+"/fcards")
        #except FileNotFoundError
        #call(["git", "clone", "https://github.com/17liamnaddell/fcards-python", sets + "/fcards"])
        #return "", ""
