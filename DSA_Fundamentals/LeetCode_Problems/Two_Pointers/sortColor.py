class Solution:
    def SortColor (self, nums:list[int]) -> None:
        low , mid , high = 0, 0, len(nums)-1
        while mid <= high:
            if nums[mid] == 0:
                nums[low] , nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif (nums[mid] == 1):
                mid += 1
            else:
                nums[high] , nums[mid] = nums[mid], nums[high]
                high -= 1
obj = Solution()
tests = [
    [2,1,0], [1,0,1,2]
]
for test in tests:
    print(obj.SortColor(test))
print(tests)