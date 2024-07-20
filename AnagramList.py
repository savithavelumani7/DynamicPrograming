a=list(map(str,input().split()))
used=[False]*len(a)
c=[]
for i in range(0,len(a)):
  if not used[i]:
    mat=sorted(a[i])
    used[i]=True
    b=[a[i]]
    for j in range(i+1,len(a)):
      if not used[j] and mat==sorted(a[j]):
        b.append(a[j])
        used[j]=True
    c.append(b)
c.sort(key=len)
print(c)
