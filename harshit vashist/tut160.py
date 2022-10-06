# any() all()
from xml.dom.minidom import Element


n1 = [2,4,6,8]
n2 = [1,2,3,4,5,6]
print(all([i%2==0 for i in n1 ]))
print(any([i%2==0 for i in n1 ]))