# Problem: Two Sum (LeetCode #1)
# Approach: HashMap (dictionary in Python)



class Solution:
    def twoSum(self, nums, target):

        notebook = {}

        for i, num in enumerate(nums):

            needed = target - num

            if needed in notebook:
                return [notebook[needed], i]

            notebook[num] = i