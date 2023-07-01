'''
Statement:
	Given a string s, find the length of the longest substring without repeating characters.

Algorithm Used:
	Dynamic Sized Sliding Window

Data Structures Used:
	Dictionary
	String

Solution:
	Time Complexity: O(n)
	Space Complexity: O(n)
'''

class Solution:
	def lengthOfLongestSubstring(self, string: str) -> int:
		chars = {} # current characters in a set
		left = 0 # to check the current left of the string
		result = 0

		for right in range(len(string)):
			if string[right] in chars and chars[string[right]] >= left: # character repeated in the sliding window
				left = chars.pop(string[right]) + 1 # remove leftmost character from current string
				
			chars[string[right]] = right
			result = (right - left + 1) if (right - left + 1) > result else result

		return result