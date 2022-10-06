def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(6)

print(mydoubler(4))