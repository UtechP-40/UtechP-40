# Exercise 13: Find the factorial of a given number
# factorial = n*n-1*n-1*n-1....n=1
n =int(input("enter any number : "))
factorial = 1

for i in range(1,n+1):
    factorial = factorial * i
print(factorial)