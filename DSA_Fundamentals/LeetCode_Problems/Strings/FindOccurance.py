class Solution:
    def findIndexOccurence(self, haystack:str, needle: str) -> int:
        n , m = len(haystack), len(needle)
        if m == 0:
            return 0
        for i in range(n-m+1):
            if haystack[i:i+m]==needle:
                return i
        return -1
items = [("sadbutsad" , "sad") , ("leetcode" , "leeto")]

obj = Solution()
for item, value in items:
    print(f"Result : {obj.findIndexOccurence(item,value)}")