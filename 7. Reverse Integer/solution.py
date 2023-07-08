'''
Statement:
	Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
	Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Data Structures Used:
	Integer
	Boolean

Solution:
	Time Complexity: O(n) -> n is number of digits in the number
	Space Complexity: O(1)
'''

class Solution:
	def reverse(self, x: int) -> int:
		reversed_num = 0
		negative = False

		if x == 0:
			return  x
		
		elif x < 0:
			negative = True
			x = abs(x)

		while x!=0:
			reversed_num = (reversed_num * 10) +  (x % 10)
			x //= 10

			if (negative and reversed_num>(2**31)) or (reversed_num>((2**31)-1)):
				return 0

		if negative:
			return -1 * reversed_num

		return reversed_num