# function returning function
def func1():
    def func2():
        print("message")
    return func2()
func1()
