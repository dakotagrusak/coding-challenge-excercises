'''
Question 2
    Level 1

Question:
    Write a program which can compute the factorial of a given numbers.
    The results should be printed in a comma-separated sequence on a single line.

Input Fortmat:
    8

Output Format:
    40320

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.

'''
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

n = int(input())
print(factorial(n))
