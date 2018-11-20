# coding: utf8
import os

class CurrentDirPrinter:
    @staticmethod # only needs adding when want to call from instance as well as class
    def printDir():
        cwd = os.getcwd()
        print(cwd)

def main():
    CurrentDirPrinter.printDir()

if __name__ == "__main__":
	main()
