# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        slow,fast = head,head
        if fast.next.next is None:
            fast.next = None
            return head
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            prev = slow
            slow = slow.next
        prev.next = slow.next

        return head
        
            