#!/usr/bin/env python

from colorama import Fore

maximum_number = 50


def isPrime(value):
    for i in range(2, value):
        if value % i == 0:
            return False
        else:
            continue
    return True


def main():
    print("Starting to compute prime numbers up to " + str(maximum_number))

    for i in range(1, maximum_number):
        if isPrime(i):
            # print('Number ' + str(i) + ' is prime.')
            print(Fore.GREEN + 'Number ' + str(i) + ' is prime.')
        else:
            # continue
            # print('Number ' + str(i) + ' is not prime.')
            print(Fore.RESET + 'Number ' + str(i) + ' is not prime. Here are all the dividers:')
            for ii in range(1, i + 1):
                if i % ii == 0:
                    print("\n" + str(ii))


if __name__ == "__main__":
    main()
