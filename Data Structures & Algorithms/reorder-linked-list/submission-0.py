# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        # we need to split the list into two halves
        # First half of list / End Half of list
        # Then we need to pop values from alternating list
        # To do this, we need a fast and a slow pointer

        slow,fast = head,head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        slow.next = None
        prev = None

        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        first = head
        second = prev

        while second:
            temp = first.next
            temp2 = second.next
            first.next = second
            second.next = temp
            first = temp
            second = temp2






        