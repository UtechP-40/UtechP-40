# filter function
# map and filter function are itrable but only once
l =[1,2,3,4,5,6,7,8]
evens = filter(lambda a:a%2==0,l)
print(*evens)