n=int(input("enter the n value"))
for i in range(n-2,-1,-1):
    print(" "*(n-i-1)+"*"*(2*i+1))
