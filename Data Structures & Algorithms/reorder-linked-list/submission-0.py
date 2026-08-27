# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = fast = head
        # first find the middle
        while(fast and fast.next):
            slow = slow.next
            fast = fast.next.next
        #reverse the 2nd half
        second = slow.next
        prev = slow.next = None
        while(second):
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt
        #now 
        first,second = head,prev
        while(second):
            # first we are saving both next values
            temp1,temp2 = first.next,second.next

            first.next = second
            second.next = temp1

            first = temp1
            second = temp2





        

        

        
        