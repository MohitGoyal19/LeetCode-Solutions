'''
Statement:
	Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

	You may assume that each input would have exactly one solution, and you may not use the same element twice.

	You can return the answer in any order.

Data Structures Used:
	List
	Dictionary

Solution:
	Time Complexity: O(n)
	Space Complexity: O(n)
'''

class Solution:
	def twoSum(self, nums: list[int], target: int) -> list[int]:
		values = {}
		for _ in range(len(nums)):
			if target - nums[_] in values:
				return [values[target-nums[_]], _]

			else:
				values[nums[_]] = _