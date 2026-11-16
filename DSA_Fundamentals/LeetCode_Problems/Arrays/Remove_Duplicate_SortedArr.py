class Solution:

    def removeDuplicateSortedArr(self, nums : list[int]) -> int :
        if not nums:
            return 0
        slow = 0
        for fast in range(1, len(nums)):
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]
        return slow + 1
        

lst = [1,1,1,2,2,3,3,3,3,3,4,4,4,4,4,4,5,5,5,5,5,5,5,5,5,5,5,5,6,6,6,6,6,6,6,6]
obj = Solution()
x = obj.removeDuplicateSortedArr(lst)
print(x)
