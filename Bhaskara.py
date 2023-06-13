x=int(input())

for x in range(x):
 z=input()
 a3,b3,c3=z.split("+")
 a2,a4=a3.split("x")
 b2,b4=b3.split("x")
 b=float(b2)
 a=float(a2)
 c=float(c3)
 delta = (b ** 2) - 4 * a * c
 x1 = (-b + delta ** (1 / 2)) / (2 * a)
 x2 = (-b - delta ** (1 / 2)) / (2 * a)
 if(delta<0):
  print("\nTest {}:".format(x+1),z)
  print("SEM RESPOSTA")
 elif(x1==x2):
   print("\nTest {}:".format(x+1),z)
   print("X = {:.2f}".format(x1))
 else:
  print("\nTest {}:".format(x+1),z)
  print("X1 = {:.2f}".format(x1))
  print("X2 = {:.2f}".format(x2))