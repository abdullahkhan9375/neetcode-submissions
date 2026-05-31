# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1:
            return l2
        if not l2:
            return l1
        
        dummy = head = ListNode()
        curr1 = l1
        curr2 = l2
        carry = 0
        while curr1 or curr2 or carry:
            l1 = curr1.val if curr1 else 0
            l2 = curr2.val if curr2 else 0
            val = l1 + l2 + carry
            carry = val // 10
            val = val % 10 
            tmp = ListNode(val = val)
            head.next = tmp
            head = head.next
            curr1 = curr1.next if curr1 else None
            curr2 = curr2.next if curr2 else None
        return dummy.next

