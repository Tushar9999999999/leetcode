# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l1 = []
        curr = head
        while curr:
            l1.append(curr)
            curr = curr.next
        a, b = 0, len(l1)-1
        target = len(l1)-n
        if target == 0:
            return head.next
        l1[target-1].next = l1[target].next
        return head
