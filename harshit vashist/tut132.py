l = [1,2,[1,3,4],43434,433,3,34]
v = [str(v) for v in l if (type(v)==int or type(v)==float)]
print(v)