#User function Template for python3
from collections import defaultdict
from collections import deque

class Solution:
    def numProvinces(self, adj, V):
        # code here 
        visited = set()
        graph = defaultdict(list)
        for i in range(len(adj)):
            for j in range(i + 1, len(adj)):
                if adj[i][j] == 1:
                    graph[i + 1].append(j + 1)
                    graph[j + 1].append(i + 1)
        
        def bfs(start_point, graph, visited):
            queue = deque()
            queue.append(start_point)
            visited.add(start_point)
            
            while queue:
                x = queue.popleft()
                for i in graph[x]:
                    if i not in visited:
                        visited.add(i)
                        queue.append(i)
        
        count = 0
        for i in range(1, V + 1):
            if i not in visited:
                bfs(i, graph, visited)
                count += 1
        return count

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        V=int(input())
        adj=[]
        
        for i in range(V):
            temp = list(map(int,input().split()))
            adj.append(temp);
        
        ob = Solution()
        print(ob.numProvinces(adj,V))
# } Driver Code Ends