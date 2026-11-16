# Pascal Triangle ::-->>

class Solution:
    def pascal_triangle(self, numRow : int) -> list[list[int]]:
        triangle : list[list[int]] = []

        for i in range(numRow):
            row = [1] * (i + 1)
            for j in range(1, i):
                row[j] = triangle [i-1][j-1] + triangle[i-1][j]
            triangle.append(row)
        return triangle

obj = Solution()
print(obj.pascal_triangle(7))
