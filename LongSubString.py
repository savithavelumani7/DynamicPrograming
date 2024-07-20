def substr(s):
  char_dict={}
  start=0
  max_str=""
  for end in range(0,len(s)):
    if s[end] in char_dict:
      start = char_dict[s[end]]+1
    char_dict[s[end]]=end
    if end-start+1>len(max_str):
      max_str=s[start:end+1]
  return max_str
s=str(input())
result=substr(s)
print(result)