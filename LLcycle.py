class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def has_cycle(head):
    if not head or not head.next:
        return False
    
    slow = head
    fast = head.next
    
    while slow != fast:
        if not fast or not fast.next:
            return False
        slow = slow.next
        fast = fast.next.next
    
    return True

def create_linked_list_with_cycle(values, pos):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    cycle_node = None if pos == -1 else head
    for i in range(1, len(values)):
        current.next = ListNode(values[i])
        current = current.next
        if i == pos:
            cycle_node = current
    if pos != -1:
        current.next = cycle_node
    return head

values = list(map(int,input().split()))
pos = int(input())
head = create_linked_list_with_cycle(values, pos)
print(has_cycle(head))  

