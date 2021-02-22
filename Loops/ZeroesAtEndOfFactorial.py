'''
You have to print the number of zeros at the end of the factorial of n.

For example, 3! = 6. The number of zeros are 0. 5! = 120. The number of zeros at the end are 1.

Hint: Think about which numbers multiplication leads to a 0 at the end
'''

def Met(n):
    res = 0
    i = 5
    while(i<= n):
        res += n//i
        i*= 5
    print(res)    
          
