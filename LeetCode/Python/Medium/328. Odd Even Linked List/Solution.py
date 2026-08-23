# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        elif head.next is None or head.next.next is None:
            return head
        else:
            odd,even,even_head = head,head.next,head.next
            while even and even.next:
                odd.next = odd.next.next
                even.next = even.next.next

                odd,even = odd.next,even.next
            odd.next = even_head
            return head
        

        