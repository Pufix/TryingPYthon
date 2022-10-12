def prime(n):
    if n==2:
        return True
    if n<2:
        return False
    if n%2==0:
        return False
    i=3
    ok = True
    while i*i <= n:
        if n%i == 0:
            ok = False
            break
        i+=2
    return ok
def ap2(n):
    if n%2==1 or n<3:
        print("There aren't 2 primes that add up to N")
    else:
        if prime(n-2):
            print ("2+"+str(n-2)+"="+str(n))
        else:
            for j in range (3,int(n/2+1),2):
                if prime(j) and prime(n-j):
                    print (str(j)+"+"+str(n-j)+"="+str(n))
                    break
ap2(1500)
