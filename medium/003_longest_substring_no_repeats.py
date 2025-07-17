# 3. Medium: Longest Substring Without Repeating Characters

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # if the input string is empty, the longest substring without repeating characters is 0.
        if not s:
            return 0
        
        # initialize a set to store characters in the current window.
        char_set = set()
        # initialize the left pointer of the sliding window.
        left = 0
        # initialize the maximum length found so far to 0.
        max_length = 0
        
        # iterate with the right pointer of the sliding window.
        for right in range(len(s)):
            # if the character at the right pointer is already in the set,
            # it means we have a repeating character.
            # we need to shrink the window from the left until the repeating character is removed.
            while s[right] in char_set:
                # remove the character at the left pointer from the set.
                char_set.remove(s[left])
                # move the left pointer to the right.
                left += 1
            
            # add the current character (at the right pointer) to the set.
            char_set.add(s[right])
            
            # calculate the current window's length (right - left + 1)
            # and update max_length if the current length is greater.
            max_length = max(max_length, right - left + 1)
            
        # return the maximum length found.
        return max_length
