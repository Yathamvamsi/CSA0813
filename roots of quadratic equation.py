a=int(input("enter the a value"))
b=int(input("enter the b value"))
c=int(input("enter the c value"))
d=(b*b-4*a*c)
if(d==0):
    print("same and real roots")
elif(d>0):
    print("different real roots")
else:
    print("imaginary roots")
