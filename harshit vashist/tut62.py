name = "Pradeep Pandey"
total = ""
for i in range(len(name)):
    if name[i] not in total:
        total += name[i]
        print(name[i]," : ",name.count(name[i]))
