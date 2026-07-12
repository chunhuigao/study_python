# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(0)
        p = head
        t = 0
        while l1 or l2:
            count = 0
            if l1 and l2:
                count = l1.val + l2.val + t
            elif l1:
                count = l1.val + t
            elif l2:
                count = l2.val + t
            else:
                count = t
            if count >= 10:
                p.next = ListNode(count - 10)
                t = 1
            else:
                p.next = ListNode(count)
                t = 0
            p = p.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        if t:
            p.next = ListNode(1)
            
        return head.next