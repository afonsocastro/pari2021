#!/usr/bin/env python

class Complex:

    def __init__(self, r, i):
        self.r = r  # store real part in class instance
        self.i = i  # store imaginary part in class instance

    def add(self, y):
        self.r = self.r + y.r
        self.i = self.i + y.i
        return self

    def multiply(self, y):
        (self.r, self.i) = (self.r*y.r - self.i*y.i, self.i*y.r + self.r*y.i)
        return self

    def __str__(self):# esta funcao serve para fazer o print
        return str(self.r) + "+" + str(self.i) + "i" if self.i >= 0 else str(self.r) + str(self.i) + "i"


def main():
    # declare two instances of class two complex numbers as tuples of size two
    c1 = Complex(5, 3)  # use order when not naming
    c2 = Complex(i=7, r=-2)  # if items are names order is not relevant

    # Test add
    print(c1)  # uses the __str__ method in the class
    c1.add(c2)
    print(c1)  # uses the __str__ method in the class

    # test multiply
    print(c2)  # uses the __str__ method in the class
    c2.multiply(c1)
    print(c2)  # uses the __str__ method in the class


if __name__ == '__main__':
    main()