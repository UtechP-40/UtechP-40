#lambda expression 
add = lambda a,b: a+b
last_char = lambda s:s[-1]
print(add(2,4))
print(last_char("pradeep"))
func = lambda s: True if len(s)>5 else False
print(func("pradeep"))