from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        result_head = n =ListNode(0)
        while(l1 or l2 or carry):
            val1=val2=0
            if l1:
                val1 = l1.val
                l1 = l1.next
            if l2:
                val2 = l2.val
                l2 = l2.next
            carry, val = divmod(val1 + val2 + carry, 10)
            n.next = ListNode(val)
            n = n.next
        return result_head.next
