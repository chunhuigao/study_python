class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        p = head.next
        head.next = self.swapPairs(p.next)
        p.next = head
        return p
    
h = ListNode(1,ListNode(2,ListNode(3,ListNode(4))))
result = Solution().swapPairs(h)
print(result.val,result.next.val,result.next.next.val,result.next.next.next.val)
