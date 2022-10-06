clist = ['Canada','USA','Mexico','Australia']
for i in range(len(clist)):
    print(f"{i} : {clist[i]}")
print("-----------USING ENUMERATE FUNCTION--------------")
for pos,name in enumerate(clist):
    print(f"{pos} : {name}")