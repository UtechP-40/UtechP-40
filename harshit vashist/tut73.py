def func(num1,num2,num3):
    if num1 > num2>num3:
        print("num1 is greatest")
    elif num2 >num1>num3:
        print("num2 is greatest")
    else:
        print("num3 is greatest")
num1 = int(input("enter 1st number : "))
num2 = int(input("enter 2nd number : "))
num3 = int(input("enter 3rd number : "))
func(num1,num2,num3)