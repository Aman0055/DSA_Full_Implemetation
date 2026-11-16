class Solution:
    def Contains_Duplicate(self, nums:list[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return True
lst = [112,32,432,564,756,123,435,435,112,564,564,32,32,32,32,32,32,0,1,1,1,1,1]
obj = Solution()
x = obj.Contains_Duplicate(lst)
print(x)