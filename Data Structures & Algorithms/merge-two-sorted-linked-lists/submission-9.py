# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1

        
        c1 = list1
        c2 = list2
        curr = ListNode()
        head = curr
        idx = 0
        while c1 or c2:
            if not c1:
                curr.val = c2.val
                c2 = c2.next
            elif not c2:
                curr.val = c1.val
                c1 = c1.next
            elif c1.val >= c2.val:
                curr.val = c2.val
                c2 = c2.next
            else:
                curr.val = c1.val
                c1 = c1.next
            idx += 1
            if not c1 and not c2:
                return head
            curr.next = ListNode()
            curr = curr.next
        return head