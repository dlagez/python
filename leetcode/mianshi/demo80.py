# https://leetcode.cn/problems/remove-duplicates-from-sorted-array-ii/
# 给你一个有序数组 nums ，请你 原地 删除重复出现的元素，
# 使得出现次数超过两次的元素只出现两次 ，返回删除后数组的新长度。
# 不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。

# 第一由于递增，所以新的数字只要与前两个数字不同，就把它搬到当前指针。
class Solution:
    def removeDuplicates(self, nums):
        i = 2
        for j in range(2, len(nums)):
            if nums[j] != nums[i - 2]:
                nums[i] = nums[j]
                i += 1
        return i  

if __name__ == '__main__':
    solution = Solution()
    list = [1, 1, 1, 2, 2, 3]
    result = solution.removeDuplicates(list)
    print(result)