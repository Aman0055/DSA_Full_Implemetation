def moveZero(nums : list[int]) -> None:
    insert_position = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            return nums[insert_position] , nums[i] == nums[i] , nums[insert_position]
        insert_position += 1
lst = [1,2,3,4,5,6,7,2,4,5,3,3,0,0,3,3,0,7,6]
x = moveZero(lst)
print(x)