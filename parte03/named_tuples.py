#!/usr/bin/env python

from collections import namedtuple

Complex = namedtuple('Complex', ['r', 'i'])


def addComplex(x, y):
    return Complex(x.r + y.r, x.i + y.i)


def multiplyComplex(x, y):
    return Complex(x.r*y.r - x.i*y.i, x.i*y.r + x.r*y.i)


def printComplex(x):
    print(str(x.r) + "+" + str(x.i) + "i")


def main():
    # define two complex numbers as tuples of size two
    c1 = Complex(5, 3)  # use order when not naming
    c2 = Complex(i=7, r=-2)  # if items are names order is not relevant
    print('c1 = ' + str(c1)) # named tuple looks nice when printed

    # Test add
    c3 = addComplex(c1, c2)
    printComplex(c3)
    # test multiply
    printComplex(multiplyComplex(c1, c2))


if __name__ == '__main__':
    main()