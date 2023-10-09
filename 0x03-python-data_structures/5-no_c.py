#!/usr/bin/python3
def no_c(my_string):
    """Remove all characters c and C from a string."""
    copy = [i for i in my_string if i != 'c' and x != 'C']
    return ("".join(copy))
