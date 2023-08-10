class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        numRows = len(matrix)
        numCols = len(matrix[0])
    
        transposedMatrix = [[0 for _ in range(numRows)] for _ in range(numCols)]
    
        for rowInd in range(numRows):
            for colInd in range(numCols):
                transposedMatrix[colInd][rowInd] = matrix[rowInd][colInd]
                
        return transposedMatrix
