# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return None

        #when we have started backtracking through recurse,
        #we have access to the current node and the next node,
        #meaning we can set the next nodes 'next' pointer to cur
        #and set the cur pointers next node to null.
        cur = head

        #if not at end of list, continue recursion
        if head.next:
            cur = self.reverseList(head.next)
            head.next.next = head 
        head.next = None

        return cur

            

        