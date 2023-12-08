#User function Template for python3
from collections import defaultdict
from typing import List
class Solution:
    def mergeDetails(self, details : List[List[str]]) -> List[List[str]]:
        # code here
        V = n
        
        def find(parent, i):
            if parent[i] != i:
                parent[i] = find(parent, parent[i])
            return parent[i]
        
        def union(parent, rank, x, y):
            x_rep = find(parent, x)
            y_rep = find(parent, y)
            if rank[x_rep] < rank[y_rep]:
                parent[x_rep] = y_rep
            elif rank[y_rep] < rank[x_rep]:
                parent[y_rep] = x_rep
            else:
                parent[y_rep] = x_rep
                rank[x_rep] += 1
        
        parent = [i for i in range(V)]
        rank = [0 for i in range(V)]
        
        map = defaultdict(int)
        for i in range(V):
            for j in range(1, len(details[i])):
                if details[i][j] in map:
                    union(parent, rank, map[details[i][j]], i)
                else:
                    map[details[i][j]] = i
        
        res = [[] for i in range(V)]
        for key, value in map.items():
            p = find(parent, value)
            res[p].append(key)
        
        ans = []
        for i in range(V):
            if len(res[i]) == 0:
                continue
            temp = []
            temp.append(details[i][0])
            list.sort(res[i])
            for mail in res[i]:
                temp.append(mail)
            ans.append(temp)
            
        return ans
            
#{ 
 # Driver Code Starts
#Initial Template for Python 3

   
from typing import List

if __name__=="__main__":
    T = int(input())
    for t in range(T):
        
        n = int(input())
        details = []
        for i in range(n):
            detail = []
            name, m = map(str, input().strip().split())
            m = int(m)
            detail.append(name)
            l = list(map(str, input().strip().split()))
            detail.extend(l)
            details.append(detail)

        obj = Solution()
        ans = obj.mergeDetails(details)
        ans.sort()
        print('[', end = '')
        for i in range(len(ans)):
            print('[', end = '')
            for j in range(len(ans[i])):
                if j != len(ans[i]) - 1:
                    print(ans[i][j], end = ', ')
                else:
                    print(ans[i][j], end = '')
            if i != len(ans) - 1:
                print(end = '], ')
            else:
                print(end = ']')
        print(']') 

        
# } Driver Code Ends