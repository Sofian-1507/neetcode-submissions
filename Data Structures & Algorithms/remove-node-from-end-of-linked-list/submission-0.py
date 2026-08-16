# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        N=0
        curr = head 
        while curr : 
            N+=1
            curr=curr.next
        prev= None 
        now = head
        if N-n == 0:
            return head.next

        for i in range(N-n):
            prev = now 
            now =now.next
        
        prev.next = now.next 

        return head