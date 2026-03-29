# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head
        # slow finds midpoint, fast finds end of list
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Reverse the slow list
        cur = slow.next
        L2 = slow.next = None
        while cur:
            temp = cur.next
            cur.next = L2
            L2 = cur
            cur = temp

        # Reorder 
        L1 = head
        while L1 and L2:
            temp1 = L1.next
            temp2 = L2.next
            L1.next = L2
            L2.next = temp1
            L1 = temp1
            L2 = temp2

