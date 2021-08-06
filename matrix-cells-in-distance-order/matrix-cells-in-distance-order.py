class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        arr = [[i,j] for i in range(R) for j in range(C)]
        return sorted(arr, key = lambda x: abs(r0 -x[0]) + abs(x[1]-c0))