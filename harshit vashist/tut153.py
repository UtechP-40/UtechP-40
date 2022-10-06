# map function
from itertools import count


l = [2,3,4,5]
square = list(map(lambda i:i**2 ,l))
p=[i**2 for i in l]
print(p,square)
clist = ['Canada','USA','Mexico','Australia']
a = map(len,clist)
for i in a:
    print(i)