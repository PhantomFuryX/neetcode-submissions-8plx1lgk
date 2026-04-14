# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        current = head
        middle = head
        end = head

        while end and end.next:
            middle = middle.next
            end = end.next.next

        sl = middle.next
        prev =None
        middle.next = None

        while sl:
            nextnode = sl.next
            sl.next = prev
            prev = sl
            sl = nextnode
        
        first = head
        second = prev

        while second:
            tmp1 =first.next
            tmp2 = second.next

            first.next = second
            second.next = tmp1

            first = tmp1
            second = tmp2
        


        



        