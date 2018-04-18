import numpy as np


class Solution(object):
    def islandPerimeter(self, grid):
        grid_x = ['0'+''.join(str(_) for _ in row)+'0' for row in grid]
        """
        This is pretty straighforward.
        '0' + ''.[0,1,0,0] + '0' = [0,0,1,0,0,0]
        """

        grid_y = ['0'+''.join(str(_) for _ in col)+'0' for col in zip(*grid)]
        """
        This is a little hard to understand.
        1. *grid converts that 2d array to the comma separated arrays.
        e.g., [[1,2,3],[4,5,6],[7,8,9]] -> (1,2,3), (4,5,6), (7,8,9)
        2. zip takes each elements one by one
        e.g., zip((1,2,3), (4,5,6), (7,8,9)) -> [1,4,7], [2,5,9], [3,6,9]
        3. for col in [[1,4,7], [2,5,9], [3,6,9]]:
        obviously, the col is the list of [1,4,7], [2,5,9], [3,6,9]
        """

        return sum([row.count('01')+row.count('10') for row in grid_x+grid_y])


grid = [[0, 1, 0, 0],
        [1, 1, 1, 0],
        [0, 1, 0, 0],
        [1, 1, 0, 0]]

print(grid)
print(np.array(grid))
print(*grid)

hoge = Solution()
hoge.islandPerimeter(grid)
