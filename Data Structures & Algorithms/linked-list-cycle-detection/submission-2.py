# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head.next == None or head.next.next == None:
            return False
        slow = head
        fast = head.next.next
        while fast:
            if slow == fast:
                return True
            if fast.next == None or fast.next.next == None:
                return False
            fast = fast.next.next
            slow = slow.next
        return False