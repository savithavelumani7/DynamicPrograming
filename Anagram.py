
def anagram(s,t):
  if(sorted(s)==sorted(t)):
    return True
  else:
    return False
s=str(input())
t=str(input())
result=anagram(s,t)
print(result)