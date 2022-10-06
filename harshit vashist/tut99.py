def string_rev(string):
    a = []
    for i in string:
        a.append(i[-1::-1])
    return a
string = input("enter your words with white spaces : ").split()
print(string_rev(string))
