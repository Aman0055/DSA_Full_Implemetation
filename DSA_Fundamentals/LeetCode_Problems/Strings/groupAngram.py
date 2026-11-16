from collections import defaultdict
from typing import List
class Solution:
    def groupAngram(self, strs:List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for s in strs:
            key = ' '.join(sorted(s))
            groups[key].append(s)
        return list(groups.values())
lists = ["eat","tea","tan","ate","nat","bat"]
obj = Solution()
print(obj.groupAngram(lists))

