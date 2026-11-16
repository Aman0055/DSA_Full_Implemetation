class Solution:
    def set_matrix_zeros(self, matrix : list[list[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        row , col = set(), set()

        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    row.add(i)
                    col.add(j)

        for i in range(m):
            for j in range(n):
                if i in row or j in col:
                    matrix[i][j] = 0

obj = Solution()
list1 = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
list2 = [[1,2,3,4],[0,1,2,3],[2,3,4,0]]
x = obj.set_matrix_zeros(list1)
y = obj.set_matrix_zeros(list2)
print(list1)
print(list2)
