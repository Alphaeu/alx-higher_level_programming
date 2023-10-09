#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    """ Check if idx is negative or out of range"""
    if idx < 0 or idx >= len(my_list):
        return my_list  # Return the same list if idx is invalid

    """Create a new list without the element at the specified index"""
    updated_list = [my_list[i] for i in range(len(my_list)) if i != idx]
    return updated_list
