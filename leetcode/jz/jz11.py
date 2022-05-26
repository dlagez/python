class Solution:
    def minArray(self, numbers) -> int:
        low, high = 0, len(numbers) - 1
        while low < high:
            pivot = low + (high - low) // 2
            # mid 小于 最右边的值，所以mid到right是有序的，所以最小值在mid的左边
            if numbers[pivot] < numbers[high]:
                high = pivot
            elif numbers[pivot] > numbers[high]:
                low = pivot + 1
            else:
                # 由于 mid = right 所以right不可能是最小值
                high -= 1
        return numbers[low]

# numbers = [1,3,5]
numbers = [2,2,2,0,1]

solution = Solution()
low = solution.minArray(numbers)