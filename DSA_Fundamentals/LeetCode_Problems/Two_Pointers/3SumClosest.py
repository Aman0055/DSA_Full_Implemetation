class Solution:
    def ThreeSumClosest(self, nums:list[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        closest = nums[0] + nums[1] + nums[2] 
        for i in range(0, n):
            left , right = i + 1, n-1
            while left < right:
                current = nums[i] + nums[left] + nums[right]
                if abs(current-target) < abs(closest-target):
                    closest = current
                if current == target:
                    return current
                elif current < target:
                    left +=1 
                else :
                    right -= 1
        return closest
obj = Solution()
list = [
    ([-1, 2, 1, -4], 1),
    ([0, 0, 0], 1),
    ([1, 1, 1, 0], -100),
]
for key , value in list:
    print(f"Three sum closest :{key}, {value}, --> {obj.ThreeSumClosest(key,value)}")
    
