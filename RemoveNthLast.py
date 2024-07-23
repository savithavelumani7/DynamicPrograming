class L:
  def __init__(self,val=0,next=None):
    self.val=val
    self.next=next
def createnode(elements):
  head=L(elements[0])
  current=head
  for ele in elements[1:]:
    current.next=L(ele)
    current=current.next
  return head
def remove(head,n):
  dummy=L(0)
  dummy.next=head
  first=dummy
  second=dummy
  for _ in range(n+1):
    first=first.next
  while first:
    first=first.next
    second=second.next
  second.next=second.next.next
  return dummy.next
def printlist(head):
  current=head
  while current:
    print(current.val,end=" ")
    current=current.next
  print("None")

elements=list(map(int,input().split()))
n=int(input())
head=createnode(elements)
result=remove(head,n)
printlist(result)