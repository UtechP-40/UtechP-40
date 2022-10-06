def my_map(func,l):
    c =[]
    for i in l:
        c.append(func(i))
    return c
def square(a):
    return a**2
l = [2,3,4,5,6]
print(my_map(square,l))
# we can also add lambda expression here like
print(my_map(lambda a:a**2,l))