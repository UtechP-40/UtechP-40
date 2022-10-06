#x = {i:i**2 for i in range(1,11) }
#print(x)
name = "harshit vashishth"
s = {s:name.count(s) for s in name}
s.pop(' ')
v  = {s:name.count(s) for s in name}
print(s,v)