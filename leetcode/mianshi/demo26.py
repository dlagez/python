# https://leetcode.cn/problems/remove-duplicates-from-sorted-array-ii/
# 给你一个有序数组 nums ，请你 原地 删除重复出现的元素，
# 使得出现次数超过两次的元素只出现两次 ，返回删除后数组的新长度。
# 不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。

# 输入：nums = [1,1,1,2,2,3]
# 输出：5, nums = [1,1,2,2,3]
# 解释：函数应返回新长度 length = 5, 并且原数组的前五个元素被修改为 1, 1, 2, 2, 3 。 
# 不需要考虑数组中超出新长度后面的元素。

# nums[i] != nums[j-1] 说明i比j大，所以i是新出现的数字，把它加入到结果中
class Solution:
    def removeDuplicates(self, nums):
        j = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[j-1]:
                nums[j] = nums[i]
                j += 1
        return j

