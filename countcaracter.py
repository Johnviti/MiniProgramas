from itertools import count
from re import X

char= input("")
lista=[]
for i in char:
    lista.append(i)
lista.sort(reverse=True)
x=1
for i in lista:
  if i!=x:
   print(i, lista.count(i))
   x=i
  
  
