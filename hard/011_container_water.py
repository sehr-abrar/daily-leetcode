# 11: Hard: Container with Most Water

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # initialize two pointers and max area
        left = 0
        right = len(height) - 1
        max_area = 0

        # move pointers toward each other
        while left < right:
            # calculate current area
            h = min(height[left], height[right])
            w = right - left
            area = h * w

            # update max area if needed
            max_area = max(max_area, area)

            # move the pointer at the shorter line
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area
