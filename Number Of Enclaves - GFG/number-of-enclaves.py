#User function Template for python3
import sys
from typing import List
sys.setrecursionlimit(10**8)

class Solution:    
    def numberOfEnclaves(self, mat: List[List[int]]) -> int:
        # code here
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(x, y):
            if x < 0 or x >= len(mat) or y < 0 or y >= len(mat[0]) or mat[x][y] == 0:
                return
            mat[x][y] = 0
            for i, j in directions:
                dfs(x + i, y + j)
                
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if (i in {0, len(mat) - 1} or j in {0, len(mat[0]) - 1}) and mat[i][j] == 1:
                    dfs(i, j)
        
        count = 0
                    
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 1:
                    count += 1
                    
        return count

#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__ == "__main__":
    for _ in range(int(input())):
        n, m = map(int,input().strip().split())
        grid = []
        for i in range(n):
            grid.append([int(i) for i in input().strip().split()])

        obj=Solution()
        print(obj.numberOfEnclaves(grid))
# } Driver Code Ends