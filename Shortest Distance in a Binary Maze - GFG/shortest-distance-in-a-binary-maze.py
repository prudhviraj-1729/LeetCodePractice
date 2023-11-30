#User function Template for python3

from typing import List
from collections import defaultdict
from collections import deque
import heapq

class Solution:
    
    def shortestPath(self, grid: List[List[int]], source: List[int], destination: List[int]) -> int:
        # code here

        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        
        priority_queue = [(0, tuple(source))]
        visited = set()
        
        distances = [[float("inf") for j in range(len(grid[0]))] for i in range(len(grid))]
        distances[source[0]][source[1]] = 0
        
        while priority_queue:
            
            current_distance, current_node = heapq.heappop(priority_queue)
            
            if current_node in visited:
                continue
            
            visited.add(current_node)
            
            if current_node == tuple(destination):
                return distances[current_node[0]][current_node[1]]
            
            for i, j in directions:
                p, q = current_node
                if p + i >= 0 and p + i < len(grid) and q + j >= 0 and q + j < len(grid[0]) and grid[p + i][q + j] == 1:
                    new_distance = distances[p][q] + 1
                    if distances[p + i][q + j] > new_distance:
                        distances[p + i][q + j] = new_distance
                        heapq.heappush(priority_queue, (new_distance, (p + i, q + j)))
        return -1
                




#{ 
 # Driver Code Starts
#Initial Template for Python 3

         
if __name__=="__main__":
    for _ in range(int(input())):
        n,m=map(int,input().strip().split())
        grid=[]
        for i in range(n):
            grid.append([int(i) for i in input().strip().split()])
        source = [0] * 2
        source[0], source[1] = map(int,input().strip().split())
        destination = [0] * 2
        destination[0], destination[1] = map(int,input().strip().split())
        obj=Solution()
        print(obj.shortestPath(grid, source, destination))
# } Driver Code Ends