"""
Title: main.py
author: Leonardo Arcanjo
Description: The entry is a array unimodal, that descrease and then increase. The script returns the index of
minor number in the array.
Input: A integer numbers array
Ouput: The index of minor number
"""


def turningNumber(array):
    """
    This function identifies the turning number index
    :param array: string
    :return i: integer
    """
    array = array.split(" ")

    # it converts from string to integer
    for i in range(len(array)):
        array[i] = int(array[i])

    # it identifies the turning number and returns the index
    for i in range(1, len(array) - 1):
        if array[i] < array[i - 1] and array[i] < array[i + 1]:
            return i
        else:
            pass


if __name__ == "__main__":
    lista = "10 9 8 7 6 1 2 3 4 5"
    index = turningNumber(lista)
    print(index)
