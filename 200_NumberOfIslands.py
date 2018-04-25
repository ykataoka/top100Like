class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        
        """
        Key Point
         - Initailization check_grid [[None]*m]*n makes it really bad!
           check_grid[0][0] = 'hoge' will change all the 1st element of the row vectors!!
        http://sonickun.hatenablog.com/entry/2014/06/13/132821
        """
        if grid == []:
            return 0
        n, m = len(grid), len(grid[0])
        cnt = 0
        # check_grid = [[None]*m]*n  # DO NOT USE THIS!!
        check_grid = [[None for i in range(m)] for j in range(n)]
        for x in range(m):
            for y in range(n):
                if (check_grid[y][x] == None) and (grid[y][x] == "1"):
                    self.dfs(grid, check_grid, y, x)
                    cnt += 1
        return cnt

    def dfs(self, grid, check_grid, y, x):
        """
             A
             ^
        B <- N -> D
             /
             C
        """
        n, m = len(grid), len(grid[0])
        check_grid[y][x] = 1
        # Pattern A
        if (y-1) >= 0 and check_grid[y-1][x] == None and grid[y-1][x] == "1":
            self.dfs(grid, check_grid, y-1, x)
        # Pattern B
        if (x-1) >= 0 and check_grid[y][x-1] == None and grid[y][x-1] == "1":
            self.dfs(grid, check_grid, y, x-1)
        # Pattern C
        if (y+1) <= n-1 and check_grid[y+1][x] == None and grid[y+1][x] == "1":
            self.dfs(grid, check_grid, y+1, x)
        # Pattern D
        if (x+1) <= m-1 and check_grid[y][x+1] == None and grid[y][x+1] == "1":
            self.dfs(grid, check_grid, y, x+1)
