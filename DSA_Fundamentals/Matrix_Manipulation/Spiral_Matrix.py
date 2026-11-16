class Solution:

    def spiral_matrix(self, matrix:list[list[int]]) -> list[int]:
        if not matrix or not matrix[0]:
            return []

        top , buttom = 0, len(matrix)-1
        left , right = 0, len(matrix[0])-1
        result :list[int] = []

        while top <= buttom and left <= right:
            for i in range(left, right + 1):
                result.append(matrix[top][i])
            top += 1

            for j in range(top, buttom + 1):
                result.append(matrix[j][right])
            right -= 1

            if top <= buttom:
                for i in range(right, left-1, -1):
                    result.append(matrix[buttom][i])
                buttom -= 1

            if left <= right:
                for j in range(buttom, top - 1, -1):
                    result.append(matrix[j][left])
                left += 1

        return result
obj = Solution()
lst=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print(obj.spiral_matrix(lst))
                