class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zr=set()
        zc=set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    zr.add(i)
                    zc.add(j)
        for i in zr:
            for j in range(len(matrix[0])):
                matrix[i][j]=0
        for i in zc:
            for j in range(len(matrix)):
                matrix[j][i]=0
                    