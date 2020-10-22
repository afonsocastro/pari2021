#!/usr/bin/python

from time import time, ctime
from math import sqrt
from colorama import Fore
from colorama import Back
from colorama import Style

#confirmar se esccreve no repositorio bfd

def main():
    print("This is" +  Fore.RED + " Ex1" + Fore.RESET + " the current date is " + Back.LIGHTYELLOW_EX + ctime() + Style.RESET_ALL )

    tic = time()#guarda o tempo qdo chama a variavel tic
    for i in range(0, 50000001):
        sqrt(i)
    toc = time()#guarda o tempo qdo chama a variavel toc

    print("Ellapsed time " + str(toc-tic) + " seconds")


if __name__ == "__main__":
    main()