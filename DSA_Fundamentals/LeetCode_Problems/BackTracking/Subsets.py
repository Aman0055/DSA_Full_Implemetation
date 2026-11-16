# Subsets :

class solution:
    def subsets(self, nums : list[int]) -> list[list[int]]:
        result = [[]]
        for num in nums:
            result += [subset + [num] for subset in result]
        return result
obj = solution()
print(obj.subsets([1,2,3,4,5]))