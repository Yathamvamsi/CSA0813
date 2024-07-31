import array
sum=0
x=[1,2,3,4,5]
a=array.array("i",[])
a.fromlist(x)
for i in a:
    sum=sum+i
print(sum)
