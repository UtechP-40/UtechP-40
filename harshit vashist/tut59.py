num0 = int(input("ENTER from where the table shoud start TABLES YOU WANT : "))
num = int(input("ENTER TO HOW MANY TABLES YOU WANT : "))
for a in range(num0,num+1):
    print(f"Table of {a}")
    for i in range(10):
        print(f"{a} * ",i+1," : ",(i+1)*a)
    print("\n")
    print("\n")