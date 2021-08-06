class Solution {
    public int numIslands(char[][] grid) {
        int count = 0;
        for (int x = 0; x < grid.length; x ++) {
            for (int y = 0; y < grid[0].length; y++) {
                if (grid[x][y] == '1') {
                    count++;
                    clear(grid,x,y);
                }
            }
        }
        return count;
    }
    
    public void clear(char[][] grid, int x, int y) {
        if (x < 0 || y < 0 || x >= grid.length || y >= grid[0].length) {
            return;
        }
        if (grid[x][y] == '0') {
            return;
        }
        
        grid[x][y] = '0';
        
        clear(grid, x + 1, y);
        clear(grid, x - 1, y);
        clear(grid, x , y + 1);
        clear(grid, x , y - 1);
    }
}