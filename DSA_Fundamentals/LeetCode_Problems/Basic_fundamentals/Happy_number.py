class Solution:
    def Happy_Number(self, n : int) -> bool:
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = sum(int(digit) ** 2 for digit in str(n))
        return n == 1

obj = Solution()
for n in [19, 7, 2, 89, 45, 67]:
    print(f"Element : {n}, is a happy no or not : {obj.Happy_Number(n)}")