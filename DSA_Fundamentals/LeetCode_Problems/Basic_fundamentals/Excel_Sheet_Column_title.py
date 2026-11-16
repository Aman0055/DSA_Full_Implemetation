class Solution:
    def Excel_Sheet(self, columnNumber : int) -> str:
        result = []
        while columnNumber > 0:
            columnNumber -= 1
            reminder = columnNumber % 26
            result.append(chr(ord("A")+ reminder))
            columnNumber //= 26
        return "".join(reversed(result))
obj = Solution()
for col in [1,26,28, 0, 701]:
    print(f"Excel_Sheet Column:{col} , after getting -> {obj.Excel_Sheet(col)}")
