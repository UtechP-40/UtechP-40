# this program by for loop
num = input("Enter numbers : ")
len = len(num)
total = 0
for i in range(len):
    total += int(num[i])
    i +=1
print(total)