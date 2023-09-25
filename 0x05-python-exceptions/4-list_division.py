#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    """
    takes two lists and creates a new list with result of divison and 
    handles errors and prints them to stdout
    """
    x = 0
    new_list = []
    result = 0
    for x in range(0, list_length):
        try:
            result = (my_list_1[x] / my_list_2[x])
        except TypeError:
            result = 0
            print("wrong type")
        except ZeroDivisionError:
            result = 0
            print("division by 0")
        except IndexError:
            result = 0
            print("out of range")
        finally:
            new_list.append(result)
    return new_list
