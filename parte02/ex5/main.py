#!/usr/bin/env python
# --------------------------------------------------
# A simple python script to print hello world!
# Miguel Riem Oliveira.
# PARI, Setember 2020.
# --------------------------------------------------
from copy import deepcopy


def countNumbersUpTo(stop_char):
    """
    Pythonic version!
    :param stop_char:
    :return:
    """
    inputs = [] #cria lista para alocar os inputs do teclado

    while True:
        char = raw_input('Enter a char (press ' + stop_char + ' to finish):')
        if char == 'X':
            break
        else:
            inputs.append(char) # faz o append dos inputs que vao sendo inseridos

    print('Here is the list of all your inputs: ' + str(inputs))

    # Ex 5a Processing of list of inputs
    total_numerics = 0
    for input in inputs:
        if input.isdigit():
            total_numerics += 1
    print('Total numeric inputs is ' + str(total_numerics)) # cria string com a adicao de duas parte, uma delas dinamica

    # Ex 5b
    numeric_inputs = [] #cria lista vazia
    for input in inputs:
        if input.isdigit():
            numeric_inputs.append(int(input))  # add new element to list

    print('Numeric inputs:' + str(numeric_inputs))

    # Ex 5c
    dict_other = {} #cria dicionario vazio
    for idx, input in enumerate(inputs): #enumerate ira retornar a posicao e o valor
        if not input.isdigit():
            dict_other[str(idx)] = input  # add new key-value to dictionary

    print('dict_other:' + str(dict_other))

    # Ex 5d
    sorted_numeric_inputs = deepcopy(numeric_inputs) #garande a duplicacao/copia completa
    # sorted_numeric_inputs = numeric_inputs #o python assim faz um apontador
    sorted_numeric_inputs.sort()
    print('sorted numeric inputs: ' + str(sorted_numeric_inputs))

    print('numeric inputs (again): ' + str(numeric_inputs))


def main():
    # ex4 a)
    # char = raw_input('Enter a char:')
    # print('You have entered  ' + char)
    # printAllCharsUpTo(char)

    # ex4 b)
    # readAllUpTo('X')

    # ex4 c)
    countNumbersUpTo('X')


if __name__ == '__main__':
    main()