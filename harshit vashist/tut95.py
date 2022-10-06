def square(numbers):
    cat = []
    for i in numbers:
         cat.append(i*i)
    return cat

t = input("enter any numbers ").split()
d = []
for i in t:
    d.append(int(i))
print(square(d))