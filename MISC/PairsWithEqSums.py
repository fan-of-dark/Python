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

def check(lst):
    return (lst[0] < lst[2] and lst[1] != lst[3] and lst[1] !=lst[2] and len(set(lst))== 4 and lst[1] > lst[0] and lst[3] > lst[2])

class Solution:
    def equal(self, A):
        
        dic = {}
        lst = []
        Flag = True
        for i in range(len(A)-1):
            for j in range(i+1,len(A)):
                add = A[i]+A[j]
                if add in dic:
                    dic[add].append(i)
                    dic[add].append(j)
                    lst.append(dic[add])
                else:
                    dic[add] = [i,j]
        lst =  list(filter(lambda x:len(x) >= 4,lst))
        lst = [i[:4] for i in lst]
        lst = list(filter(check,lst))
        if len(lst) != 0:
            return min(lst)
        else:
            return []

            
                        
            
                        
