from itertools import count


sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]
l = []
for i in sample_list:
    if i not in l:
        l.append(i)
for i in l:
    print(i," : ",sample_list.count(i))
