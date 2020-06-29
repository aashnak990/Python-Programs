n=int(input("enter a number"))
for i in range(1,n+1):
   d= str(i)
   o= str(oct(i))[2:]
   h= str(hex(i))[2:]
   h= h.upper()
   b= str(bin(i))[2:]
   print(d ,'    ', o ,'      ',h,'             ', b)
