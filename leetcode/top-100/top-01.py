class Solution:
    def twoSum(self, nums, target):
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []
    
    def twoSum2(self, nums, target):
        hashtable = dict()
        for i, num in enumerate(nums):
            if target - num in hashtable:
                return [hashtable[target - num], i]
            hashtable[nums[i]] = i
        return []

if __name__ == "__main__":
    # nums = [2,7,11,15]
    # target = 9
    # solution = Solution()
    # result = solution.twoSum(nums, target)
    # print(result)

    nums = [2,7,11,15]
    target = 9
    solution = Solution()
    result = solution.twoSum2(nums, target)
    print(result)
