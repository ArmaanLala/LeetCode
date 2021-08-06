class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for table in matrix:
            if (target in table):
                return True
        return False