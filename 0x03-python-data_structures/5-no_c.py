#!/usr/bin/python3
def no_c(my_string):
    """Remove all characters c and C from a string."""
    filtered_string = []
    for i in my_string:
        if i != 'c' and i != 'C':
            filtered_string.append(i)
    return " ".join(filtered_string)
