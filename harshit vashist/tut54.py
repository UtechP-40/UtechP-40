name = input("enter your name : ")
i  = 0
temp_var = ""
while i < len(name):
    if name[i] not in temp_var:
        a= i+1
        print(name[i],end=" : ")
        print(name.count(name[i]))
        temp_var += name[i]
    i = i+1