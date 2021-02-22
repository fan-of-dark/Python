'''
Consider a sequence of the form 0, 1, 1, 2, 4, 7, 13, 24, 44, 81, 149...

Complete the given method solve which takes as parameter an integer n and prints the nth term of the above sequence. The nth term will fit in an integer value.

Hint: Does this pattern look familiar? Remember the logic for Fibonacci series?

Example Input: 5
Output: 4
Example Input: 8
Output: 24
Example Input: 11
Output: 149
'''

def solve(n):
    # write your code here
    a = 0
    b = 1
    c = 1
    for i in range (n-3):
        res = a+b+c
        a,b,c = b,c,res
    print(res)    
