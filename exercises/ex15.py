# Exercise 17: Find the sum of
# the series upto n terms
# Write a program to calculate 
# the sum of series up to 
# n term. For example, if n =5 
# the series will become 
# 2 + 22 + 222 + 2222 + 22222 = 24690
n = 5
nt = 2
z = "2"
total = [nt]
final =0
for i in range(n-1):
        nt = str(nt)+ z
        total.append(int(nt))
for k in total:
    final += k
print(final)