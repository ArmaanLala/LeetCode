class Solution:
    def numSquares(self, n: int) -> int:
        squares = []
        starting = 1
        while starting**2 <= n:
            squares.append(starting**2)
            starting += 1 
        queue = {n}
        count = 0
        while queue:
            tempQueue = set()
            count += 1
            for i in queue:
                for j in squares:
                    if (i == j):
                        return count
                    if (i < j):
                        break
                    tempQueue.add(i - j)
            queue = tempQueue
        return count