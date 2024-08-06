#square
n=int(input('enter the n value'))
for i in range(1,n):
    for j in range(1,n):
        print('*',end='')
    print("")
    
#diamond   
n=int(input("enter the n value"))
for i in range(n):
    print(" "*(n-i-1)+"*"*(2*i+1))
for i in range(n-2,-1,-1):
    print(" "*(n-i-1)+"*"*(2*i+1))

#upper triangle
    n=int(input("enter the n value"))
for i in range(n):
    print(" "*(n-i-1)+"*"*(2*i+1))

#lower triangle
n=int(input("enter the n value"))
for i in range(n-2,-1,-1):
    print(" "*(n-i-1)+"*"*(2*i+1))
    
#hallowsquare
    n=int(input("enter the value:"))
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1:
            print("* ",end="")
        else:
            print("  ",end="")
    print()

