"""
Given an array A of integers, find the index of values that satisfy A + B = C + D, where A,B,C & D are integers values in the array.

Note:

Return the indices A1 B1 C1 D1, so that
A[A1] + A[B1] = A[C1] + A[D1]
A1 < B1, C1 < D1
A1 < C1, B1 != D1, B1 != C1

If there are more than one solutions, then return the tuple of values which are lexicographical smallest.
Assume we have two solutions
S1 : A1 B1 C1 D1 ( these are values of indices int the array )
S2 : A2 B2 C2 D2

S1 is lexicographically smaller than S2 iff

A1 < A2 OR
A1 = A2 AND B1 < B2 OR
A1 = A2 AND B1 = B2 AND C1 < C2 OR
A1 = A2 AND B1 = B2 AND C1 = C2 AND D1 < D2

Input :

A = [3, 4, 7, 1, 2, 9, 8]

Output :
[0, 2, 3, 5] (O index)

Note : If no solution is possible, return an empty list.
"""

def calc(A,A1,C1):
    doop = A.copy()
    doop1 = doop[A1+1:]
    doop2 = doop[C1+1:]
    for j in range(len(doop1)):
        B1 = doop1[j]
        for k in range(len(doop2)):
            D1 = doop2[k]
            if D1 != B1 and  A[A1]+B1 == A[C1] +D1:
                return (A1,A.index(doop1[j]),C1,A.index(doop2[k]))

class Solution:
    def equal(self, A):
        # write your method here
        lst = []
        for i in range(len(A)-1):
            for j in range(i+1,len(A)):
                tup = calc(A,i,j)
                if tup != None:
                    lst.append(tup)
            
        if len(lst) != 0:
            return min(lst)
        else:
            return []
            
                        
