#User function Template for python3

from collections import defaultdict
class Solution:
    def accountsMerge(self, accounts):
        # Code here
        V = len(accounts)
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
            for j in range(1, len(accounts[i])):
                if accounts[i][j] in map:
                    union(parent, rank, map[accounts[i][j]], i)
                else:
                    map[accounts[i][j]] = i
        
        res = [[] for i in range(V)]
        for key, value in map.items():
            p = find(parent, value)
            res[p].append(key)
        
        ans = []
        for i in range(V):
            if len(res[i]) == 0:
                continue
            temp = []
            temp.append(accounts[i][0])
            list.sort(res[i])
            for mail in res[i]:
                temp.append(mail)
            ans.append(temp)
        
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        n = int(input())
        accounts = []
        for i in range(n):
            cntEmails = int(input())
            nameEmails = input().split()
            accounts.append(nameEmails)
        ob = Solution()
        res = ob.accountsMerge(accounts)
        res.sort()
        print('[', end = '')
        for i in range(len(res)):
            print('[', end = '')
            for j in range(len(res[i])):
                if j != (len(res[i]) - 1):
                    print(res[i][j], end = ', ')
                else:
                    print(res[i][j], end='')
            if (i != len(res) - 1):
                print('], ')
            else:
                print(']', end = '')
        print(']')
# } Driver Code Ends