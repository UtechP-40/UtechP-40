#take input from user as string
# create function is_palindrom 
              #which checks that if we reverse the string will it be same
# return a boolion value
def is_palindrom(word):
    return word == word[-1::-1]

word  = input("Enter a word : ")
print(is_palindrom(word))