num = input("enter anu number : ")
num2 = num[-1::-1]
if num == num2:
    print(f"original number {num}\nYes. given number is palindrome number")
elif num != num2:
    print(f"original number {num}\nNo. given number is not palindrome number")
else:
    print("print wrong input")
