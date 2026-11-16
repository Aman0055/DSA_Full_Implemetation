class Solution:
    def generateParenthesis(self, n: int) -> list[str]:

        def helper(result, string, left, right):
            if left == 0 and right == 0:
                result.append(string)
                return

            if left > 0:
                helper(result, string + '(', left - 1, right)
            if right > 0 and left < right:
                helper(result, string + ')', left, right - 1)

        result = []
        helper(result, '', n, n)
        return result

obj = Solution()
print(obj.generateParenthesis(3))
print(obj.generateParenthesis(4))
print(obj.generateParenthesis(5))