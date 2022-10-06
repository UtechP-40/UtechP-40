#Exercise 3: Print characters from a string that are present at an even index number
#Write a program to accept a string from the user and display characters that are present at an even index number.
#
#For example, str = "pynative" so you should display ‘p’, ‘n’, ‘t’, ‘v’.
word = input("type any word : ")
length = len(word)
i = 0
while i<=length :
    print(word[i])
    i = i+2
