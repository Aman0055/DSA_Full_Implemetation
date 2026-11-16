class Solution:
    def RotatedSortedArray(self, nums:list[int], target: int) -> int:
        left , right = 0, len(nums)-1
        while left <= right:
            mid = (left + right)// 2
            if nums[mid] == target:
                return mid 
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <=nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1 

items = [
    ([3,4,5,6,1,2],1) , ([3,5,6,0,1,2],4) , ([4,5,6,7,0,1,2],3) , ([4,5,6,7,0,1,2],0)
]
obj = Solution()
for item , value in items:
    print(f"Result : {obj.RotatedSortedArray(item, value)}")