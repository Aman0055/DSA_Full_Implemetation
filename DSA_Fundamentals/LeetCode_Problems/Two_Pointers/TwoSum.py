def twoSum(nums: list[int], target : int) -> list[int]:
    seen = {}
    for i , num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []
lst = [2,8,7,5,0,9]
x = twoSum(lst,9)
print(x)


