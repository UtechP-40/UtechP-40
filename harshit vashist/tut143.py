def hek(num , *args):
    if args:
        return [i**num for i in args]
    return "hey you didn't pass any args"
p = [2,3,4]
print(hek(2,*p))