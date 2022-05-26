import collections


class Solution:
    def firstUniqChar(self, s: str) -> str:
        fre = collections.Counter(s)
        for i, ch in enumerate(s):
            if fre[ch] == 1:
                return ch
        return ' '


l = "leetcode"
solution = Solution()
first = solution.firstUniqChar(l)
