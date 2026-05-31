# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = {}
        seen2 = {}
        while head:
            if head.val in seen and head.next in seen2:
                return True
            else:
                seen[head.val] = head.val
                seen2[head.next] = head.next
            head = head.next
        return False