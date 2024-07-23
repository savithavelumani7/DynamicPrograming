class L:
  def __init__(self,val=0,next=None):
    self.val=val
    self.next=next
def createnode(elements):
  if not elements:
    return None
  head=L(elements[0])
  current=head
  for ele in elements[1:]:
    current.next=L(ele)
    current=current.next
  return head
def merge(list1,list2):
  dummy=L()
  tail=dummy
  while list1 and list2:
    if list1.val<=list2.val:
      tail.next=list1
      list1=list1.next
    else:
      tail.next=list2
      list2=list2.next
    tail=tail.next

    if list1:
      tail.next=list1
    else:
      tail.next=list2
  return dummy.next

def printLL(merge_head):
    result=[]
    current=merge_head
    while current:
      result.append(current.val)
      current=current.next
    return result




element1=list(map(int,input().split()))
element2=list(map(int,input().split()))
list1=createnode(element1)
list2=createnode(element2)
head=merge(list1,list2)
print(printLL(head))