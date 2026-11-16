# class Solution:
#     def searchRange(self, nums: list[int], target: int) -> list[int]:
#         left = self.findLeft(nums, target)
#         right = self.findRight(nums, target)
#         return [left, right]

#     def findLeft(self, nums: list[int], target: int) -> int:
#         left, right = 0, len(nums) - 1
#         while left <= right:
#             mid = (left + right) // 2
#             if nums[mid] < target:
#                 left = mid + 1
#             else:
#                 right = mid - 1
#         if left < len(nums) and nums[left] == target:
#             return left
#         return -1

#     def findRight(self, nums: list[int], target: int) -> int:
#         left, right = 0, len(nums) - 1
#         while left <= right:
#             mid = (left + right) // 2
#             if nums[mid] <= target:
#                 left = mid + 1
#             else:
#                 right = mid - 1
#         if right >= 0 and nums[right] == target:
#             return right
#         return -1

class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        def search_bound(is_left: bool) -> int:
            left , right = 0, len(nums) - 1
            result = -1
            while left <= right:
                mid = (left + right)//2
                if nums[mid] == target:
                    result = mid
                    if is_left:
                        right = mid - 1
                    else:
                        left = mid + 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return result
        return [search_bound(True), search_bound(False)]

items  = [
    ([5,7,7,8,8,10], 8), ([5,7,7,8,8,10], 6), ([], 0), ([1], 1)
]
obj = Solution()
for item, value in items:
    print(f"Result :{obj.searchRange(item, value)}")