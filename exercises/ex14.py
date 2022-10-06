# Exercise 16: Calculate the cube of all numbers from 1 to a given number
number = int(input("enter any : "))
cube = 0
for i in range(number):
    cube = i*i*i
    print(cube)
    cube = 0