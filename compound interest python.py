p=eval(input("enter the price"))
r=eval(input("enter the rate"))
t=eval(input("enter the time"))
n=eval(input("enter the no.of times is interest is compounded"))
compound_interest=p*(1+r/n)**n*t-p
print("compound interest=",compound_interest)
             
       
