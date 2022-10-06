#zip function
user = ['user1' , 'user2' , 'user3' ]
name = ['Pradeep' , 'sandeep' , 'harshit']
last_name = ['pandey', 'pandey','vashitha']
#zip method cat take any number of parameters
p = zip(user,name,last_name)
print(*p)
