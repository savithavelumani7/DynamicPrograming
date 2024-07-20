nums=list(map(int,input().split()))
k=int(input())
def second(a):
  return a[1]
table={}
for num in nums:
  table[num]=0
for num in nums:
  table[num]+=1
result=sorted(table.items(),key=second,reverse=True)

for i in range(0,k):
  print(result[i][0],end=" ")
