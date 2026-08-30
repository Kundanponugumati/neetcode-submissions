# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        temp = l1
        num1 = 0
        digit1 = 0
        while(temp):
            num1 = num1 + (10**digit1)*temp.val
            temp = temp.next
            digit1 +=1
        temp = l2
        num2 = 0
        digit2 = 0
        while(temp):
            num2 +=(10**digit2)*temp.val
            temp = temp.next
            digit2 +=1
        print(num1,num2)
        num = num1+num2
        num = str(num)
        dummy_node = ListNode(-1)
        temp = dummy_node
        for i in range(len(num)-1,-1,-1):
            temp.next = ListNode(int(num[i]))
            temp = temp.next
        return dummy_node.next


        


        