'''
Statement: 
	You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
	
	You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Data Structures Used:
	Linked-List
	Pointers

Solution:
	Time Complexity: O(n)
	Space Complexity: O(n)
'''

# Definition for singly-linked list.
class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next

class Solution:
	def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
		head = ListNode()
		node = head

		carry = 0
		while l1 or l2 or carry:
			number1 = l1.val if l1 else 0
			number2 = l2.val if l2 else 0
			
			added = number1 + number2 + carry
			carry = added // 10
			added = added % 10

			node.next = ListNode(added)
			
			l1 = l1.next if l1 else None
			l2 = l2.next if l2 else None
			
			node = node.next

		return head.next