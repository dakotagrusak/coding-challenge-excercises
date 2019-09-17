'''
Task
    You are given a space separated list of numbers. 
    Your task is to print a reversed NumPy array with the element type float.

Input Format
    A single line of input containing space separated numbers.

Output Format
    Print the reverse NumPy array with type float.

Sample Input
    1 2 3 4 -8 -10

Sample Output
    [-10.  -8.   4.   3.   2.   1.]
'''

import numpy as np

arr = np.array(input().split(" "), float)
reversed_arr = np.flipud(arr)

print(reversed_arr)
# def arrays():
#     # complete this function
#     # use numpy.array
#     numpy.array(input().strip().split(' '), float)

# print(arrays())

