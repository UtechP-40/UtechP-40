#def tag(*args):
#    k=[]
#    c=0
#    for i in zip(*args):
#        k.append(sum(i)/len(i))
#        c = 0
#    return k
l1,l2,l3,l4 = [1,2,3,4],[4,5,6,4],[7,8,9,5],[6,10,11,12]
#print(tag(l1,l2,l3))
t = lambda *args:[(sum(i)/len(i)) for i in zip(*args)]
print(t(l1,l2,l3,l4))