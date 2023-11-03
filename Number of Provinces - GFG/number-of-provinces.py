#User function Template for python3
from collections import defaultdict

class Solution:
    def numProvinces(self, adj, V):
        # code here 
        visited_array = ["false" for i in range(V + 1)]
        graph_list = defaultdict(list)
        for i in range(len(adj)):
            for j in range(i + 1, len(adj)):
                if adj[i][j] == 1:
                    graph_list[i + 1].append(j + 1)
                    graph_list[j + 1].append(i + 1)
        
        def dfs(index, graph_list, visited_array):
            visited_array[index] = "true"
            for i in graph_list[index]:
                if visited_array[i] == "false":
                    dfs(i, graph_list, visited_array)
        
        count = 0
        for i in range(1, len(visited_array)):
            if visited_array[i] == "false":
                dfs(i, graph_list, visited_array)
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