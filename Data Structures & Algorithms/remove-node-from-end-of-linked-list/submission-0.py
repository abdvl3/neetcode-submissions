# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        dummy = ListNode(0, head)          # handles removing the real head

        def helper(node):
            if not node:
                return 0                   # past the end
            pos = helper(node.next) + 1    # this node's position from the end
            if pos == n + 1:               # we're the node *before* the target
                node.next = node.next.next
            return pos

        helper(dummy)
        return dummy.next
        