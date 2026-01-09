# Given the head of a singly linked list, return the middle node of the linked list.
# If there are two middle nodes, return the second middle node.

 
# Example 1:
# Input: head = [1,2,3,4,5] Output: [3,4,5] Explanation: The middle node of the list is node 3.

# Example 2:
# Input: head = [1,2,3,4,5,6] Output: [4,5,6] Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.

# Constraints:

# The number of nodes in the list is in the range [1, 100].
# 1 <= Node.val <= 100


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Create nodes
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)

# Link nodes:
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

def middle(head):
    slow = head
    fast = head.next
    i = 1
    
    if not fast : return slow
    if not fast.next: return fast

    while True:
        if i ==2 or (i %2 == 1 and i !=1): slow = slow.next
        print(i, fast.val, slow.val)
        fast = fast.next
        if not fast: break
        
        i +=1
    
    return slow


middle(node1)



