# https://leetcode.cn/problems/letter-combinations-of-a-phone-number/
# 给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。

# 思路：回溯算法

# from itertools import combinations


from itertools import combinations
from operator import le


class Solution:
    def letterCombinations(self, digits):
        if not digits:
            return list()
        
        phoneMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(index):
            if index == len(digits):
                combinations.append("".join(combination))
            else:
                digit = digits[index]
                for letter in phoneMap[digit]:
                    combination.append(letter)
                    backtrack(index + 1)
                    combination.pop()

        combination = list()
        combinations = list()
        backtrack(0)
        return combinations

if __name__ == '__main__':
    digits = '256'
    solution = Solution()
    result = solution.letterCombinations(digits)
    print(result)