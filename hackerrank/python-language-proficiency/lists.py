'''
Tasks:
    Consider a lst (lst = []). You can perform the following commands:
        1. insert i e: Insert integer e at position i.
        2. print: Print the lst.
        3. remove e: Delete the first occurrence of integer e.
        4. append e: Insert integer e at the end of the lst.
        5. sort: Sort the lst.
        6. pop: Pop the last element from the lst.
        7. reverse: Reverse the lst.

    Initialize your lst and read in the value of  followed by  lines of commands where each command will be of the  types lsted above. Iterate through each command in order and perform the corresponding operation on your lst.

Input Format:
    The first line contains an integer, n, denoting the number of commands.
    Each line i of the n subsequent lines contains one of the commands described above.

Constraints:
    The elements added to the lst must be integers.

Output Format:
For each command of type print, print the lst on a new line.
'''

#!/usr/bin/env python
if __name__ == '__main__':
    N = int(input())

L = []

for i in range(0, N):
    tokens = input().split()

    if tokens[0] == 'insert':
        L.insert(int(tokens[1]), int(tokens[2]))
    elif tokens[0] == 'print':
        print(L)
    elif tokens[0] == 'remove':
        L.remove(int(tokens[1]))
    elif tokens[0] == 'append':
        L.append(int(tokens[1]))
    elif tokens[0] == 'sort':
        L.sort()
    elif tokens[0] == 'pop':
        L.pop()
    elif tokens[0] == 'reverse':
        L.reverse()
