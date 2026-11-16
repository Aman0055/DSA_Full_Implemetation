class Solution:
    def reverse_stringword(self, s:str) -> str:
        words = s.split()
        return ' '.join(reversed(words))
strs = "the sky is blue"
obj = Solution()
print(obj.reverse_stringword(strs))
