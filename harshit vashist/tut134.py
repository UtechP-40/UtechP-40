import imaplib


l = [1,2,3,4,5,6,7,8]
v = [i*2 if(i%2==0) else -i for i in l]
print(v)