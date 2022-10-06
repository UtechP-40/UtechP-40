def asf(num):
    a=[]
    b=[]
    c=[a,b]
    for i in num:
        if i%2==0:
            a.append(i)
        else:
            b.append(i)
    return c
number = input("enter numbers with white spaces : ").split()
num = []
for i in number:
    num.append(int(i))
print(asf(num))
