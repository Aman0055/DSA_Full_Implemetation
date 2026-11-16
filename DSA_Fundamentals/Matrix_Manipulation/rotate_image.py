def rotate_image(nums:list[list[int]]) -> list[int] :
    n = len(nums)
    left , right = 0, n-1
    for i in range(n):
        for j in range(i+1, n):
            nums[i],nums[j]=nums[j],nums[i]
    for row in nums:
        row.reverse()
    return nums
list = [[1,2,3],[4,5,6],[7,8,9]]
x = rotate_image(list)
print(f"Rotate image :{x}")
