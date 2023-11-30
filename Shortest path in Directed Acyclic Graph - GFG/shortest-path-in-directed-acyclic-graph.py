#User function Template for python3

from typing import List
import heapq
class Solution:
    def shortestPath(self, n : int, m : int, edges : List[List[int]]) -> List[int]:
        
        adj = [[] for i in range(n)]
        
        for l in edges:
            x, y, z = l
            adj[x].append([y, z])
        
        priority_queue = [(0, 0)]
        visited = set()
        
        distances = [float("inf") for i in range(n)]
        distances[0] = 0
        
        while priority_queue:
            current_distance, current_node = heapq.heappop(priority_queue)
            
            if current_node in visited: 
                continue
            
            visited.add(current_node)
            
            for neighbour_node, neighbour_distance in adj[current_node]:
                new_neighbour_distance = current_distance + neighbour_distance
                if distances[neighbour_node] > new_neighbour_distance:
                    distances[neighbour_node] = new_neighbour_distance
                    heapq.heappush(priority_queue, (new_neighbour_distance, neighbour_node))
        for i in range(len(distances)):
            if distances[i] == float("inf"):
                distances[i] = -1
        return distances
    

#{ 
 # Driver Code Starts

#Initial Template for Python 3

from typing import List




class IntMatrix:
    def __init__(self) -> None:
        pass
    def Input(self,n,m):
        matrix=[]
        #matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix
    def Print(self,arr):
        for i in arr:
            for j in i:
                print(j,end=" ")
            print()



class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n,m=map(int,input().split())
        
        
        edges=IntMatrix().Input(m, 3)
        
        obj = Solution()
        res = obj.shortestPath(n, m, edges)
        
        IntArray().Print(res)
# } Driver Code Ends