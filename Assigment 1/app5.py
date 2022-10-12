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
def ap5(n):
    if n<2:
        print("There aren't any primes bellow the given N")
    else:
        for i in range(n-1,0,-1):
            if prime(i):
                print(i)
                break
ap5(100)


