from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if(not head or not head.next):
            return None
        p1 = head
        p2 = head
        temp = None
        while(p2 and p2.next):
            temp = p1
            p1 = p1.next
            p2 = p2.next.next
        temp.next = p1.next
        del(p1)
        return head