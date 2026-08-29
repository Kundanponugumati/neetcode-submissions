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
        map = {}
        curr = head
        dummy = Node(0)
        tail = dummy
        while(curr):
            copy_node = Node(curr.val)
            map[curr] = copy_node
            tail.next = copy_node
            tail = copy_node
            curr = curr.next
        
        curr1 = head
        curr2 = dummy.next
        while(curr1):
            if curr1.random:
                curr2.random = map[curr1.random]
            curr1 = curr1.next
            curr2 = curr2.next
        return dummy.next


            
        