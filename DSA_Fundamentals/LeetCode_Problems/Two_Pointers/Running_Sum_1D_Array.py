def runningSum(nums : list[int]) -> list[int]:
    result = []
    total = 0
    for num in nums:
        total += num
        result.append(total)
    return result
lst = [1,2,3,4,4,5]
x = runningSum(lst)
print(x)