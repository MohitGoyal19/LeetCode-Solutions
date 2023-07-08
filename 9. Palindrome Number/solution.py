'''
Statement:
	Given an integer x, return true if x is a palindrome, and false otherwise.

Data Structures Used:
	Integer

Solution:
	Time Complexity: O(n) -> n is number of digits in the number
	Space Complexity: O(1)
'''

class Solution:
	def isPalindrome(self, n: int) -> bool:
		if n < 0:
			return False

		reversed_num = 0
		x = n
		while x > 0:
			reversed_num = (reversed_num * 10) + (x%10)
			x //= 10

		return reversed_num == n