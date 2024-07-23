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
def reverseLL(head):
  prev=None
  while head:
    temp=head.next
    head.next=prev
    prev=head
    head=temp
  return prev
def LLtolist(prev):
  rev_list=[]
  current=prev
  while current:
    rev_list.append(current.val)
    current=current.next
  return rev_list

elements=list(map(int,input().split()))
head=createnode(elements)
result=reverseLL(head)
print(LLtolist(result))