class Solution:
    def LongestCommonPrefix(self, str:list[str])-> list[str]:
        if not str:
            return ""
        prefix = str[0]
        for s in str[1:]:
            while not s.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix

obj = Solution()
str1= ['flower','flows','flo']
print(obj.LongestCommonPrefix(str1))