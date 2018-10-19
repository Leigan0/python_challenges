# coding: utf8
import os

class CurrentDirPrinter:

    def printDir(self):
        cwd = os.getcwd()
        print(cwd)
