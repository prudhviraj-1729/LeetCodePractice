#User function Template for python3
from collections import defaultdict
from collections import Counter
class Solution:
    def findOrder(self,alien_dict, N, K):
    # code here

        graph = defaultdict(list)
        
        for w1, w2 in zip(alien_dict, alien_dict[1:]):
            for i, j in zip(w1, w2):
                if i != j:
                    graph[i].append(j)
                    break

        V = set("".join(alien_dict))
        visited = set()
        ans = []
        
        def dfs(node):
            visited.add(node)
            for child in graph[node]:
                if child not in visited:
                    visited.add(child)
                    dfs(child)
            ans.append(node)
        
        for node in V:
            if node not in visited:
                dfs(node)
                
        if len(visited) != len(V):
            return []
            
        return ans[::-1]
        
    
    





#{ 
 # Driver Code Starts
#Initial Template for Python 3

class sort_by_order:
    def __init__(self,s):
        self.priority = {}
        for i in range(len(s)):
            self.priority[s[i]] = i
    
    def transform(self,word):
        new_word = ''
        for c in word:
            new_word += chr( ord('a') + self.priority[c] )
        return new_word
    
    def sort_this_list(self,lst):
        lst.sort(key = self.transform)

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        line=input().strip().split()
        n=int(line[0])
        k=int(line[1])
        
        alien_dict = [x for x in input().strip().split()]
        duplicate_dict = alien_dict.copy()
        ob=Solution()
        order = ob.findOrder(alien_dict,n,k)
        s = ""
        for i in range(k):
            s += chr(97+i)
        l = list(order)
        l.sort()
        l = "".join(l)
        if s != l:
            print(0)
        else:
            x = sort_by_order(order)
            x.sort_this_list(duplicate_dict)
            
            if duplicate_dict == alien_dict:
                print(1)
            else:
                print(0)


# } Driver Code Ends