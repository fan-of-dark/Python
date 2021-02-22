'''
Consider the following sequence:

1st term: 1
2nd term: 1 2 1
3rd term: 1 2 1 3 1 2 1
4th term: 1 2 1 3 1 2 1 4 1 2 1 3 1 2 1

And so on. Complete the given method solve that takes as parameter an integer n and prints the nth terms of this sequence.

Hint: Perhaps you should use a String to store the sequence? What is happening in each term of the sequence?

Example Input: 1
Output: 1
Example Input: 4
Output: 1 2 1 3 1 2 1 4 1 2 1 3 1 2 1
'''


def solve(n):
    res =  []
    for i in range(1,n+1):
        res = res + [i] +  res
    print(*res)  
