def Squares_Of_Sorted_Array(nums : list[int] ) -> list[int]:
    n = len(nums)
    result = [0] * n
    left , right = 0 , n - 1
    pos = n -1
    while left <= right:
        left_sq = nums[left] ** 2
        right_sq = nums[right] ** 2
        if left_sq > right_sq:
            result[pos] = left_sq
            left += 1
        else :
            result[pos] = right_sq
            right -= 1
        pos -= 1
    return result
lst = [-7, -2, 4,7,9,10,4,1,2]
x = Squares_Of_Sorted_Array(lst)
print(x)
