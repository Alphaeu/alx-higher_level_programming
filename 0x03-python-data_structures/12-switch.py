#!/usr/bin/python3
a = 89
b = 10

"""Switching values without using a temporary variable."""
a, b = b, a
print("a={:d} - b={:d}".format(a, b))
