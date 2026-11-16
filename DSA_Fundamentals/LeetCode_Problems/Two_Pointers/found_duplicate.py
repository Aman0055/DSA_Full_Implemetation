def found_duplicate(nums : list[int]) -> bool:
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
        return False
lst = [1,2,3,0,0,4,2,1,4]
x = found_duplicate(lst)
print(x)