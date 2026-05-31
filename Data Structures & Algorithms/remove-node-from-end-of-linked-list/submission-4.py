# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None
        
        length = 0
        ptr1 = head
        while ptr1:
            ptr1 = ptr1.next
            length += 1

        mx = length - n
        ptr1 = dummy = head
        prev = None
        if mx == 0:
            return head.next
        for i in range(mx):
            prev = ptr1
            ptr1 = ptr1.next
        
        prev.next = ptr1.next
        return dummy
