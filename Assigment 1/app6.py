def isleap(n):
    if n%4!=0:
        return False
    if n%100!=0:
        return True
    if n%400==0:
        return True
    return False
def year(y,d):
    leap=0
    if isleap(y):
        leap=1
    if d<=31:
        print("January "+str(d)+" "+str(y))
    elif d<=59+leap:
        print("February "+str(d-31)+" "+str(y))
    elif d<=90+leap:
        print("March "+str(d-59-leap)+" "+str(y))
    elif d<=120+leap:
        print("April "+str(d-90-leap)+" "+str(y))
    elif d<=151+leap:
        print("May "+str(d-120-leap)+" "+str(y))
    elif d<=181+leap:
        print("June "+str(d-151-leap)+" "+str(y))
    elif d<=212+leap:
        print("July "+str(d-181-leap)+" "+str(y))
    elif d<=243+leap:
        print("August "+str(d-212-leap)+" "+str(y))
    elif d<=273+leap:
        print("September "+str(d-243-leap)+" "+str(y))
    elif d<=304+leap:
        print("Octomber "+str(d-273-leap)+" "+str(y))
    elif d<=334+leap:
        print("November "+str(d-304-leap)+" "+str(y))
    elif d<=365+leap:
        print("December "+str(d-334-leap)+" "+str(y))
year(2020,200)