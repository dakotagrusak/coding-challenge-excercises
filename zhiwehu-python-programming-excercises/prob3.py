'''
Question 3
    Level 1

Question:
    With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included),and then the program should print the dictionary.

Input Format:
    8

Output Format:
    {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

Hints:
    In case of input data being supplied to the question, it should be assumed to be a console input.
    Consider use dict()
'''

#!/usr/bin/env python

for i in range(1,n+1):
    dict.update()

n = int(input())
print ({i : i*i for i in range(1,n+1)})
