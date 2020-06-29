import re
sum=0
handle=open('regex_sum_444943.txt')
for line in handle:
    y=re.findall('[0-9]+',line)
    for i in range(0, len(y)):
      y[i] = int(y[i])
      sum=sum+y[i]
print(sum)
