# plus one 

class Solution:
    def plusOne(self, digits : list[int]) -> list[int] :
        digits = digits[:]
        for i in range(len(digits)-1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        return [1] + digits
obj = Solution()
for digits in [[1,2,3,4], [9,9,9,9], [0,0,0,0], [9,0,1,0,9], [5,6,7,8]]:
    print(f"Digits : ({digits}) -> , Plus_One Of Digits : {obj.plusOne(digits)}")