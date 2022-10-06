def subset(set1,set2):
    set3 = set1 + set2
    set4 =[]
    for i in set3:
        if i in set1 and i in set2:
            if i not in set4:
                set4.append(i)
    return set4
set1=[1,2,3,4,5]
set2 = [2,3,6,7,8]
print(subset(set1, set2))