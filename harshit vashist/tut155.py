l =[1,2,3,4,5,6,7,8] #--list--tuples--string are itrabal
evens = filter(lambda a:a%2==0,l) #---itreator
#in this we will know how for function works
p = iter(l)
print(next(p))
print(next(p))
print(next(p))
print(next(p))
print(next(p))
print(next(p))
# this is how for loop works 
# first we converted l into a iterator but in case of filter and map we do not
# have to do this becouse they return a iterator
# proof is 
print(*evens,"\n",*p)