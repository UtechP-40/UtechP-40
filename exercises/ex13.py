# Exercise 15: Use a loop to display elements from a given list present at odd index position
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
length = len(my_list)
for i in range(length):
    if i == 0:
        continue
    elif i == 1:
        print(my_list[i])
    elif i%2 == 0:
        continue
    else:
        print(my_list[i])


    
    
    
