user = {}
user['Name'] = input("ENTER YOUR NAME : ")
user['age'] = int(input("ENTER YOUR AGE : "))
user['fav_movies'] = input("enter your fav movies : ").split()
user['fav_songs'] = input("enter your fav songs : ").split()
for i in user:
    print(i," : ",user[i])