# coding: utf8
import os

class CurrentDirPrinter:
    @staticmethod
    def printDir():
        cwd = os.getcwd()
        print(cwd)

def main():
    cwd = CurrentDirPrinter.printDir()

if __name__ == "__main__":
	main()
