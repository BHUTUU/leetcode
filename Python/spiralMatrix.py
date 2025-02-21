class Solution:
    def spiralOrder(self, matrix):
        result = []
        if not matrix:
            return result
        while matrix:
            result+=matrix.pop(0)
            if matrix and matrix[0]:
                for row in matrix:
                    result.append(row.pop())
            if matrix and matrix[0]:
                result+=reversed(matrix.pop())
            if matrix and matrix[0]:
                for i in reversed(matrix):
                    result.append(i.pop(0))
        return result

                


solInstance = Solution()
print(solInstance.spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]])) # Expected output: [1, 2, 3, 6, 9, 8, 7, 4, 5]
print(solInstance.spiralOrder([[1, 2, 3, 4, 5], [6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]))