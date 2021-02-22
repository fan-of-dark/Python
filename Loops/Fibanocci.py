def Fibanocci(n):
    if n == 1:
        print(0)
    elif n >1:
        a = 0
        b = 1
        print(a, end = " ")
        print(b, end = " ")
        for i in range(n-2):
            print(a+b,end = " ")
            c = b
            b = b + a
            a = c
            
            
    
        
    
