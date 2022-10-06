# Exercise 10: Remove duplicates from a list and create a tuple 
# and find the minimum and maximum number
sample_list = [87, 45, 41, 65, 94, 41, 99, 94]
a =[]
for i in sample_list:
    if i not in a:
        a.append(i)
print(a)
b = tuple(a)
print(b)
print("min : " , min(b))
print("max : " , max(b))