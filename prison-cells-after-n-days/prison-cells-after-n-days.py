class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        # The pattern repeats every 14 days so we dont need to recalculate every single time
        for day in range((n-1)% 14 + 1):
            newCells = [0]*len(cells)
            for i in range (len(cells)): 
                if (i - 1 < 0 or i + 1 >= len(cells)):
                    newCells[i] = 0
                else:
                    if (cells[i-1] == cells[i+1]):
                        newCells[i] = 1
                    else:
                        newCells[i] = 0
            cells = newCells
        return cells