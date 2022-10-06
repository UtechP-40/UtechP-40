def count_list(l):
    a = 0
    for i in l:
        if type(i) == list:
            a+=1
    return a
l = [1,2,3,[1,2],[4,5,6]]
print(count_list(l))