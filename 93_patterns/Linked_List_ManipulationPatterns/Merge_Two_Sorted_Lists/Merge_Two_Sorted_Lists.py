# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
# Return the head of the merged linked list.

# Example 1:
# Input: list1 = [1,2,4], list2 = [1,3,4] Output: [1,1,2,3,4,4]

# Example 2:
# Input: list1 = [], list2 = [] Output: []

# Example 3:
# Input: list1 = [], list2 = [0] Output: [0]

# Constraints:

# The number of nodes in both lists is in the range [0, 50].
# -100 <= Node.val <= 100
# Both list1 and list2 are sorted in non-decreasing order.


# Definition for singly-linked list.

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def createLLfromList(lst):
    if not lst:return []
    
    head = ListNode(lst[0])
    prev = None
    for i in range(1, len(lst)):
        curr = ListNode(lst[i])
        if i == 1: head.next = curr
        else: prev.next = curr

        prev = curr
    
    return head

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        op = []
        curr1 = list1
        curr2 = list2
        while True:
            if curr1 and curr2:
                if curr1.val < curr2.val: 
                    op.append(curr1.val)
                    curr1 = curr1.next
                elif curr1.val > curr2.val: 
                    op.append(curr2.val)
                    curr2 = curr2.next
                else:
                    op.append(curr1.val)
                    op.append(curr2.val)
                    curr1 = curr1.next
                    curr2 = curr2.next
            elif not curr1 and curr2:
                op.append(curr2.val)
                curr2 = curr2.next
            elif curr1 and not curr2:
                op.append(curr1.val)
                curr1 = curr1.next
            else: break
    
        return createLLfromList(op)

list1 = [1,2,4]
list2 = [1,3,4]    

a = Solution()
a.mergeTwoLists(createLLfromList(list1), createLLfromList(list2))