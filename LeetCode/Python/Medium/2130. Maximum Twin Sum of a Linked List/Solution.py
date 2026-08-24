# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow , fast , max_sum = head,head,0
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        prev = None
        while slow:
            next_node = slow.next
            slow.next = prev
            prev = slow
            slow = next_node
        first = head
        while prev:
            twin_sum = first.val + prev.val
            max_sum = max(max_sum,twin_sum)
            first = first.next
            prev = prev.next
        return max_sum       