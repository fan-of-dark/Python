def solve(A):
    flag = None
    for i in A:
        for j in A:
            if j != i:
                if sum(i) == sum(j):
                    print(*i)
                    print(*j)
                    flag = False
                    break
                    
        if flag == False:
            break
                    
