# Power Of Two ::::::

class Solution:
    def power_of_two(self, n : int) -> bool:
        return (n > 0) and (n & (n-1)) == 0

obj = Solution()
print(obj.power_of_two(12))
print(obj.power_of_two(16))
print(obj.power_of_two(1))
print(obj.power_of_two(-12))
print(obj.power_of_two(122))
print(obj.power_of_two(128 * 2))