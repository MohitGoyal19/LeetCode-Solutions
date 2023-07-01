# Time Complexity: O(n)
# Space Complexity: O(n)


class Solution:
	def twoSum(self, nums: list[int], target: int) -> list[int]:
		values = {}
		for _ in range(len(nums)):
			if target - nums[_] in values:
				return [values[target-nums[_]], _]

			else:
				values[nums[_]] = _