class Solution:
    def BinarySearch(self, nums:list[int], target: int)-> int:
        left , right = 0, len(nums)-1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else :
                right = mid - 1
        return -1
obj = Solution()
items = [
    ([-1,0,3,5,9,12],9) ,([-1,0,3,5,9,12],2)
] 
for item , value in items:
    print(f"Result : {obj.BinarySearch(item, value)}")