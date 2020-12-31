class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        s_length = len(s)
        if s_length == 1:
            return s
        
        start = 0
        end = start + 1
        max_length = 1
        max_substring = s[0]
        
        for start in range(s_length):
            for end in range(s_length, start, -1):
                length = end - start
                if length <= max_length:
                    break
                substring = s[start:end]
                if substring == substring[::-1] and length > max_length:
                    max_length = length
                    max_substring = substring
                    break
        return max_substring
