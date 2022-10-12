def ap4(n):
    nbr=[1]
    i=0
    while(n>0):
        nbr[i]=n%10
        i+=1
        n=int(n/10)
        nbr.append(0)
    for j in range(i):
        for l in range(j+1,i):
            if nbr[j]>nbr[l]:
                w=nbr[j]
                nbr[j]=nbr[l]
                nbr[l]=w
    n=0
    for j in range(i,-1,-1):
        n*=10
        n+=nbr[j]
    print(n)
ap4(763332)