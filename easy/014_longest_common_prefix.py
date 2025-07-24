# 14. Easy: Longest Common Prefix

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # return empty string if list is empty
        if not strs:
            return ""

        # take the first string as a base
        prefix = strs[0]

        # compare with each string in the list
        for word in strs[1:]:
            # shrink prefix until it matches the start of word
            while not word.startswith(prefix):
                prefix = prefix[:-1]
                # if prefix becomes empty, no common prefix
                if not prefix:
                    return ""

        return prefix
