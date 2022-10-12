def prime(n):
    if n<2:
        return False
    if n==2:
        return True
    if n%2==0:
        return False
    i=3
    while i*i<=n:
        if n%i==0:
            return False
        i+=2
    return True
def ap1(n):
    i=n+1
    while True:
        if prime(i):
            print(i)
            break
        i+=1
ap1(101)


