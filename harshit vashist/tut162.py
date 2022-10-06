
#advance min() max() function


#names = ['harhit' , 'pradeep','sandeep']
#print(min(names ,key = lambda x:len(x)))
students = [
    {'name' :'pradeep','score':70},
    {'name' :'sandeep','score':80},
    {'name' :'harshit','score':10}
    ]
students2 = {
    'harshit' : {'score' : 94,'age' : 19},
    'pradeep' : {'score' : 95,'age' : 18},
    'sandeep' : {'score' : 91,'age' : 20}
}
def maximum(student):
    print(student)
print(max(students2 , key = lambda student:students2[student].get('age')))
#print(max(students , key = lambda student:student['score']))
#print(maximum(students))
#maximum(students2)
