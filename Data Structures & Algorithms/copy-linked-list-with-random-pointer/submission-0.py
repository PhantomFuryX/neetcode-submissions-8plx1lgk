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

        if not head:
            return None

        nodelist = {}

        current = head
        while current:
            nodelist[current] = Node(current.val)
            current = current.next

        copyhead = head
        while copyhead:
            nodelist[copyhead].next = nodelist.get(copyhead.next)
            nodelist[copyhead].random = nodelist.get(copyhead.random)
            copyhead = copyhead.next

        return nodelist[head]