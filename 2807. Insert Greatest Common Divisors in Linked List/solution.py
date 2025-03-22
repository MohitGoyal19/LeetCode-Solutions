# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        while current:
            if current.next:
                gcd = 1
                for x in range(min(current.val, current.next.val), 0, -1):
                    if (current.val % x == 0) and (current.next.val % x == 0):
                        gcd = x
                        break

                gcd_node = ListNode(val=gcd, next=current.next)
                current.next = gcd_node

                current = gcd_node.next

            else:
                current = current.next

        return head