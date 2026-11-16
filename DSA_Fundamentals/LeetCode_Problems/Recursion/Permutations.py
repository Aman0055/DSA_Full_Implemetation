# Permutation Problem :

class Solution:

    def get_permutations(self, nums: list[int], result: list[list[int]], idx: int) -> None:
        if idx == len(nums):
            result.append(nums.copy())
            return

        for i in range(idx , len(nums)):
            nums[idx], nums[i] = nums[i], nums[idx]
            self.get_permutations(nums, result, idx + 1)
            nums[idx], nums[i] = nums[i], nums[idx]

    def permute(self, nums: list[int]) -> list[list[int]]:
        result = []
        self.get_permutations(nums, result , 0)
        return result

obj = Solution()
print(obj.permute([1,2,3,4]))
print("*" * 110)
print(obj.permute([1,2,3]))
