class Solution:
    def relativeSortArray(self, arr1: list[int], arr2: list[int]) -> list[int]:
        count = [0] * 1001

        for num in arr1:
            count[num] += 1

        result = []

        for num in arr2:
            result.extend([num] * count[num])
            count[num] = 0

        for num in range(1001):
            if count[num] > 0:
                result.extend([num] * count[num])
        
        return result

items = [
    [[2,3,1,3,2,4,6,7,9,2,19], [2,1,4,3,9,6]], [[28,6,22,8,44,17], [22,28,8,6]]
]
obj = Solution()
for arr1, arr2 in items:
    print(f"Result : {obj.relativeSortArray(arr1, arr2)}")