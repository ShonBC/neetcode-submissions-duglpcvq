# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        dummy = head
        while dummy.next:
            dummy = dummy.next
            count += 1
        if count + 1 == n:
            head = head.next
            return head
        dummy = head
        for i in range(count - n):
            dummy = dummy.next
        temp = dummy.next if dummy.next else None
        dummy.next = temp.next if temp else None
        return head
        