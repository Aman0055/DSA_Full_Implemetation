class Solution:
    def fibonacci_number(self, n : int) -> int:
        if n <= 1:
            return n
        return self.fibonacci_number(n-1) + self.fibonacci_number(n -2)
obj = Solution()
print("Fibonacci :" , obj.fibonacci_number(12))