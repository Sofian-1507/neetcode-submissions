# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast ,slow = head ,head 
        while fast and fast.next :
            fast = fast.next.next 
            slow =slow.next 
        mid =slow.next
        slow.next=None
        curr = mid 
        prev = None 
        while curr : 
            nxt = curr.next
            curr.next = prev
            prev =curr
            curr = nxt 
        l1,l2 = head,prev
        while l2:
            t1,t2 = l1.next ,l2.next 
            l1.next = l2 
            l2.next =t1
            l1,l2 =t1,t2

            