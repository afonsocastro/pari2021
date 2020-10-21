#!/usr/bin/env python
from collections import namedtuple

Complex = namedtuple('Complex', ['r', 'i'])#nova estrutura de dados named tuple

def addComplex(x, y):
    return x[0] + y[0], x[1] + y[1]

def multiplyComplex(x, y):
    return x[0]*y[0] - x[1]*y[1], x[1]*y[0] + x[0]*y[1]

def printComplex(x):
    print(str(x[0]) + "+" + str(x[1]) + "i")


def main():
    # ex2 a)

    # define two complex numbers as tuples of size two
    c1 = Complex(5, 3) #como inserir os tuplos
    c2 = Complex(r=-2, i=7)

    # Test add

    printComplex(addComplex(c1, c2))

    # test multiply
    printComplex(multiplyComplex(c1, c2))


if __name__ == '__main__':
    main()

