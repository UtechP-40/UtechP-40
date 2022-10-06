while True:
    try:
        a = int(input("Enter a number : "))
        a = a*a
    except Exception as e:
        print(e)
    else:
        print(a)