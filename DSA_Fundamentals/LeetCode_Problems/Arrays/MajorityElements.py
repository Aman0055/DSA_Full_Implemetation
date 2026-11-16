class Solution:
    def MajorityElements(self, nums:list[int]) -> int:
        candidate , count = None, 0
        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if num == candidate else -1
        return candidate

items = [
    [3,2,3], [2,2,1,1,1,2,2]
]
obj = Solution()
for item in items:
    print(f"Result : {obj.MajorityElements(item)}")
