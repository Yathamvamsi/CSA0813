def lcm():
    n1=int(input("enter the n1 value"))
    n2=int(input("enter the n2 value"))
    for i in range(n1,n2+1):
        if n1%i==0 and n2%i==0:
            gcd=i
    lcm=n1*n2/gcd
    print("lcm = ",lcm)
    print("gcd = ",gcd)
lcm()
