#!/usr/bin/python3
<<<<<<< HEAD
"""Module containing a function to print first and last name"""


def say_my_name(first_name, last_name=""):
    """ prints first and last name
        Arguments:
            @first_name: first name to be printed
            @second_name: last_name to be printed
    """

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
=======
'''
module: say_my_name
'''


def say_my_name(first_name, last_name=''):
    ''' print first and last name, make the big bucks
    Keyword arguments:
    first_name -- string
    last_name -- string
    '''

    #  ERROR MESSAGE DICT  #
    err_msg = {}
    err_msg["FirstNotStr"] = "first_name must be a string"
    err_msg["LastNotStr"] = "last_name must be a string"

    #  TESTS  #
    if type(first_name) != str:
        raise TypeError(err_msg["FirstNotStr"])
    if type(last_name) != str:
        raise TypeError(err_msg["LastNotStr"])

    #  OUTPUT  #
    print("My name is {}".format(first_name), end='')
    if len(last_name) == 0:
        print()
    else:
        print(" {}".format(last_name))
>>>>>>> 48e0916cb9b981d85ea35d6b8b6193e4b548abd7
