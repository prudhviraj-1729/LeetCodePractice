#User function Template for python3
from collections import deque

class Solution:
    def numProvinces(self, adj, V):
        # code here 
        visited_array = ["false" for i in range(V + 1)]
        graph_list = [[] for i in range(V + 1)]
        for i in range(V):
            for j in range(V):
                if adj[i][j] == 1 and i != j:
                    if j + 1 not in graph_list[i + 1]:
                        graph_list[i + 1].append(j + 1)
                    if i + 1 not in graph_list[j + 1]:
                        graph_list[j + 1].append(i + 1)
                        
        def bfs(start_point, graph_list, visited_array):
            queue = deque()
            queue.append(start_point)
            visited_array[start_point] = "true"
            while queue:
                x = queue.popleft()
                for i in range(len(graph_list[x])):
                    if visited_array[graph_list[x][i]] == "false":
                        visited_array[graph_list[x][i]] = "true"
                        queue.append(graph_list[x][i])
        
        count = 0
        for i in range(1, len(visited_array)):
            if visited_array[i] == "false":
                bfs(i, graph_list, visited_array)
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