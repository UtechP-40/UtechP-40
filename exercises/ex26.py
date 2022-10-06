# 
# Exercise 8: Iterate a given list and check if a given element exists as a key’s value in a dictionary.
#  If not, delete it from the list
#After removing unwanted elements from list [47, 69, 76, 97]
roll_number = [47, 64, 69, 37, 76, 83, 95, 97]
sample_dict = {'Jhon':47, 'Emma':69, 'Kelly':76, 'Jason':97}
l =[]
for i in roll_number:
    for b in sample_dict.values():
        if i == b:
            l.append(i)
print(l)
