#checks if the given num is prime/not
def solve(n):
    if n < 2:
        print("Not Prime")
    else:
        for i in range(2,n//2):
            if n%i == 0:
                print("Not Prime")
                break
        else:
            print("Prime")
