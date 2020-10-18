#!/usr/bin/env python

from time import time, ctime
from math import sqrt


def main():
    print("This is Ex1 and the current date is " + ctime())

    tic = time()
    for i in range(0, 50000001):
        sqrt(i)
    toc = time()

    print("Ellapsed time " + str(toc-tic) + " seconds")


if __name__ == "__main__":
    main()