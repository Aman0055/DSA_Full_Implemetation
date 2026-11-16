class Solution:
    def maxProdSubArray(self, nums:list[int])-> int:
        max_prod = min_prod = result = nums[0]
        for num in nums[1:]:
            if num < 0:
                max_prod, min_prod = min_prod, max_prod
            max_prod = max(num, num * max_prod)
            min_prod = min(num, num * min_prod)
            result = max(result, max_prod)
        return result

lst = [2,3,-2,4]
obj = Solution()
print(obj.maxProdSubArray(lst))