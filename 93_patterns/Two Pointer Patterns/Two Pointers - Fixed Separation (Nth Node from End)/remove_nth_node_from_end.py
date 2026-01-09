# Given the head of a linked list, remove the nth node from the end of the list and return its head.

# Example 1:
# Input: head = [1,2,3,4,5], n = 2 Output: [1,2,3,5]

# Example 2:
# Input: head = [1], n = 1 Output: []

# Example 3:
# Input: head = [1,2], n = 1 Output: [1]

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Create nodes
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
# node4 = ListNode(4)
# node5 = ListNode(5)

# Link nodes:
node1.next = node2
node2.next = node3
# node3.next = node4
# node4.next = node5


def removeNode(head, n):
    lag = None
    lead = head

    if not lead.next and n ==1: return None
    i = 0
    while True:
        i += 1
        lead = lead.next
        if not lead:
            if i == n: return head.next
            lag.next = lag.next.next
            break
        if i >= n: lag = lag.next if lag else head
        print(i, lead.val if lead else None, lag.val if lag else None)
    return head

removeNode(node1, 3)
