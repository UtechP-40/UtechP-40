def cap(l,**kwargs):
    return [i[-1::-1].title() if (kwargs.get('reverse_str')==True) else i.title()  for i in l]
l= ['harshit','pradeep']
print(cap(l,reverse_str = True))