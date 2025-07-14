# https://www.geeksforgeeks.org/batch/python-foundation/track/Python-Foundation-Data-Types/problem/swap-the-numbers
class Solution:
    def swap(self, a, b):
        print(b, a)

"""
or  use 3 variables:

temp = a
a = b
b = temp

or do the without 3 variables via arithmetic swap
basically store combined sum then use subtraction to extract original value
a = a + b
b = a - b
a = a - b

or bitwise swap with XOR operator
XOR (^) returns 1 when bits are different, 0 when bits are same.  it works only on integers
a = a ^ b
b = a ^ b
a = a ^ b

pythonic, tuple swap:

a, b = b, a

"""