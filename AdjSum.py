

a=list(map(int,input().split()))
target=int(input())
flag=0
for i in range(0,len(a)):
  for j in range(i+1,len(a)):
    if(a[i]+a[j]==target):
      print(i,j)
      flag=1
      break
if (flag==0):
  print('-1')
