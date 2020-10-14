#!/usr/bin/env python

maximum_number = 100

def isPerfect(value):
    """ Returns true if a number is perfect or false is a number is not perfect
    :param value: the number that is supposed to discover if is perfect or not
    :return: the boolean value
    """
    lista_divisores = []
    for i in range(1, value):
        if value % i == 0:
            lista_divisores.append(i)
        else:
            continue

    if sum(lista_divisores) == value:
        return True
    else:
        return False


def main():
    print("Starting to compute perfect numbers up to " + str(maximum_number))

    for i in range(0, maximum_number):
        if isPerfect(i):
            print('Number ' + str(i) + ' is perfect.')


if __name__ == "__main__":
    main()
