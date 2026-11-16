class Solution:

    def missing_num(self, nums : list[int]) -> int:
        n = len(nums)
        expected_num = (n * (n+1) // 2)
        actual_num = sum(nums)
        missing_no = expected_num - actual_num
        return missing_no
obj = Solution()
print(f"Missing No : {obj.missing_num([0,12,11,10,9,7,6,5,4,3,2,1])}")
print(f"Missing No : {obj.missing_num([0,11,10,9,7,6,5,4,2,1,3])}")