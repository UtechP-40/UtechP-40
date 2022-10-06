try:
    a = int(input("Enter a number : "))
    a = a*a
except Exception as e:
    print(e)
    exit()
finally:
    print("welcome here ")
    