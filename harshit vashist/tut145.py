def func(**kwargs):
    for k,v in kwargs.items():
        print(f"{k}:{v}")
d= {'name' : 'pradeep','age':19,'year':'2nd'}
func(**d)
#using all parameters
# def func1(name,*args,age=19,**kwargs)
#padk