class Solution:
    def find_pivot_index(self, nums:list[int]) -> int:
        total = len(nums)
        left_sum = 0
        for i , num in enumerate(nums):
            right_sum = total - left_sum - num
            if left_sum == right_sum:
                return i
            left_sum += num
        return -1
lst = [1,7,3,6,5,6]
obj = Solution()
x = obj.find_pivot_index(lst)
print(x)