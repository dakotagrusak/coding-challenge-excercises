'''
Question 4
    Level 1

Question:
    Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
Input Format:
    34,67,55,33,12,98
Output Format:
    ['34', '67', '55', '33', '12', '98']
    ('34', '67', '55', '33', '12', '98')
Hints:
    In case of input data being supplied to the question, it should be assumed to be a console input.
    tuple() method can convert list to tuple
'''
#!/usr/bin/env python3

# x = str(input())
x = input()

# generates a list
print(x.split(","))

# generates a tuple
# a tuple is an immutable list
print(tuple(x.split(",")))
