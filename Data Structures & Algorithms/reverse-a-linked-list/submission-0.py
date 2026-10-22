# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        if head == None:
            return None
        if head.next is None:
            print(head.val)
            return head
        
        N = head.next
        head.next = None
        ret = self.reverseList(N)
        N.next = head

        
        return ret