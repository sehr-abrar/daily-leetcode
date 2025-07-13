# 1. Easy: Two Sum

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # create a dictionary to store numbers and their indices
        seen = {}

        # loop through the list with both index and value
        for i, num in enumerate(nums):
            # calculate the number we need to find to reach the target
            complement = target - num

            # check if the complement has already been seen
            if complement in seen:
                # if yes, return the indices of the complement and current number
                return [seen[complement], i]

            # otherwise, store the current number and its index in the dictionary
            seen[num] = i

        # if no solution found, return empty
        return []
