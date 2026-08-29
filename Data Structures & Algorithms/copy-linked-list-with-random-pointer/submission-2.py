"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # add a copy of node
        temp = head
        while(temp):
            copy_node = Node(temp.val)
            copy_node.next = temp.next
            temp.next = copy_node
            temp = copy_node.next
        
        # handle random pointer
        temp = head
        while(temp):
            copy_node = temp.next
            if temp.random:
                copy_node.random = temp.random.next
            temp = temp.next.next

        # handle next pointer
        dummy_node = Node(-1)
        res = dummy_node
        temp = head
        while(temp):
            res.next = temp.next
            temp.next = temp.next.next
            res = res.next
            temp = temp.next
        return dummy_node.next


            
        