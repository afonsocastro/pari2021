#!/usr/bin/env python

from time import time, ctime
from math import sqrt
from colorama import Fore
from colorama import Back


#confirmar se esccreve no repositorio bfd
def main():
    print("This is" +  Fore.RED + " Ex1" + Fore.RESET + " the current date is " + Back.LIGHTYELLOW_EX + ctime() + Back.RESET)

    tic = time()
    for i in range(0, 50000001):
        sqrt(i)
    toc = time()

    print("Ellapsed time " + str(toc-tic) + " seconds")


if __name__ == "__main__":
    main()