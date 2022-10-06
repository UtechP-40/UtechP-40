def reverse(numbers):
    numbers.reverse()
    return numbers
t = input(" enter numbers with white space : ").split()
d = []
for i in t:
    d.append(int(i))
print(reverse(d))