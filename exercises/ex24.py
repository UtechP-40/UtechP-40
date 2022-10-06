# Exercise 6: Find the intersection (common) of two sets and remove those elements from the first set
first_set = {23, 42, 65, 57, 78, 83, 29}
second_set = {57, 83, 29, 67, 73, 43, 48}
a = []
b = []
for i in first_set:
    if i in second_set:
        a.append(i)
    else:
        b.append(i)
print(a)
print(b)