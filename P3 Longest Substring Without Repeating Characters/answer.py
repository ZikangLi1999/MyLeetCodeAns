class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == '':
            return 0
        if len(s) == 1:
            return 1
        
        count_max = 0
        ls = list(s)
        length = len(ls)
        
        for start in range(length):
            end = start + 1
            collector = {}
            collector[ls[start]] = collector.get(ls[start], 0) + 1
            
            while end < length and ls[end] != ls[start]:
                collector[ls[end]] = collector.get(ls[end], 0) + 1
                for times in collector.values():
                    if times > 1:
                        end -= 1
                        break
                end += 1
            
            count = end - start + 1
            count_max = count if count > count_max else count_max
        
        return count_max
        