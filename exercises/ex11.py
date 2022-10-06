stop = 10
a = 0
b = 1
if stop == 0:
    print(a)
elif stop ==1:
    print(a,b)
else:
    print(a,b,end = " ")
    for i in range(stop):
        c= a+b
        a=b
        b =c
        print(c,end = " ")
