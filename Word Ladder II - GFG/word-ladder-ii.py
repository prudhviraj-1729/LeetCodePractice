#User function Template for python3
from collections import defaultdict
from collections import deque
from itertools import permutations
class Solution:
    def findSequences(self, begW, endW, wordList):
        #Code here
        wordList.append(begW)

        patterns = defaultdict(set)
        for word in wordList:                                   # Creating adjacency list for patterns of words
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i + 1:]
                patterns[pattern].add(word)
                
        graph = defaultdict(set)                                # Creating adjacency list of words i.e
        for elem in patterns.values():                          # Creating a Graph of words
            for x, y in permutations(elem, 2):
                graph[x].add(y)
                
        deps = {w: -1 for w in wordList}
        deps[begW] = 0
        paths = defaultdict(list)
        paths[begW] = [[begW]]
        queue = deque([begW])
    
        while queue:
            w = queue.popleft()
            if w == endW: return paths[w]
            for neib in graph[w]:
                if deps[neib] == -1 or deps[neib] == deps[w] + 1:
                    if deps[neib] == -1:
                        queue.append(neib)
                        deps[neib] = deps[w] + 1
                    for elem in paths[w]:
                        paths[neib].append(elem + [neib])
        return []

#{ 
 # Driver Code Starts

from collections import deque 
import functools

def comp(a, b):
    x = ""
    y = ""
    for i in a:
        x += i 
    for i in b:
        y += i
    if x>y:
        return 1
    elif y>x:
        return -1 
    else:
        return 0

if __name__ == '__main__':
    T=int(input())
    for tt in range(T):
        n = int(input())
        wordList = []
        for i in range(n):
            wordList.append(input().strip())
        startWord = input().strip()
        targetWord = input().strip()
        obj = Solution()
        ans = obj.findSequences(startWord, targetWord, wordList)
        if len(ans)==0:
            print(-1)
        else:
            ans = sorted(ans, key=functools.cmp_to_key(comp))
            for i in range(len(ans)):
                for j in range(len(ans[i])):
                    print(ans[i][j],end=" ")
                print()

# } Driver Code Ends