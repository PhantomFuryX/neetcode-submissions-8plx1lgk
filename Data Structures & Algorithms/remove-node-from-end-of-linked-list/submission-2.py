# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        llen = 0
        lencal = head
        while lencal:
            llen += 1
            lencal = lencal.next
        
        print(llen)
        current = head
        if current is None:
            return

        if  llen - n == 0:
            head = current.next
            current=None
            return head

        pos = 0
        prev = None
        while current and (pos != llen - n):
            prev = current
            current = current.next
            pos += 1

        prev.next = current.next
        current= None

        return head
        


        