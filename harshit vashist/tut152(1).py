def place(clist,name):
    for p,v in enumerate(clist):
        if v ==name:
            return p

clist = ['Canada','USA','Mexico','Australia']
name = "Mexico"
print(place(clist,name))