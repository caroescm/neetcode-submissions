# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        counter = 0
        curr = head
        while curr:
            counter += 1
            curr = curr.next

        dummy = ListNode(0)
        dummy.next = head

        prev = dummy
        for _ in range(counter - n):
            prev = prev.next
        
        prev.next = prev.next.next

        return dummy.next

