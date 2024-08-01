#perfect number
import math
a=int(input("enter the a value"))
b=math.sqrt(a)
c=b**2
if c==a:
    print(a,"perfect number")
else:
    print(a,"not perfect number")
            
