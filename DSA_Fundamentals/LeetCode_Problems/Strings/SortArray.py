class Solution:
    def SortArray(self, nums:list[int]) -> list[int]:
        if len(nums) <= 1:
            return nums
        mid = len(nums) // 2
        left = self.SortArray(nums[:mid])
        right = self.SortArray(nums[mid:])

        merged = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged
items = [
    [10,9,1,1,1,2,3,1], [5,10,2,1,3], [5,2,3,1], [5,1,1,2,0,0]
]
obj = Solution()
for item in items:
    print(f"Result : {obj.SortArray(item)}")