from exceptions import InputException

AUTHORIZED_CHARS = "abcdefghijklmnopqrstuvwxyz"

def check_login(input):
    if type(input) is not str:
        raise InputException("Input must be string")
    for char in input.lower():
        if char not in AUTHORIZED_CHARS:
            raise InputException(char + " is not allowed")
        