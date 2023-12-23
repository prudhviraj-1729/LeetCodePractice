#User function Template for python3
from collections import defaultdict

class Solution:
    
    #Function to find the vertical order traversal of Binary Tree.
    def verticalOrder(self, root): 
        #Your code here
        dic = defaultdict(list)
        self.min_l, self.max_l = float("inf"), -float("inf")
        
        def dfs(root, lvl_h, lvl_v):
            self.min_l = min(lvl_h, self.min_l)
            self.max_l = max(lvl_h, self.max_l)
            
            if lvl_h in dic.keys():
                dic[lvl_h].append((lvl_v, root.data))
            else:
                dic[lvl_h] = [(lvl_v, root.data)]
                
            if root.left:  dfs(root.left,  lvl_h-1, lvl_v+1)
            if root.right: dfs(root.right, lvl_h+1, lvl_v+1)
        
        dfs(root, 0, 0)
        out = []
        for i in range(self.min_l, self.max_l + 1):
            out += [j for i,j in sorted(dic[i], key=lambda x: x[0])]
        return out





#{ 
 # Driver Code Starts
#Initial Template for Python 3

#Contributed by Sudarshan Sharma
from collections import deque
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None



# Function to Build Tree   
def buildTree(s):
    #Corner Case
    if(len(s)==0 or s[0]=="N"):           
        return None
        
    # Creating list of strings from input 
    # string after spliting by space
    ip=list(map(str,s.split()))
    
    # Create the root of the tree
    root=Node(int(ip[0]))                     
    size=0
    q=deque()
    
    # Push the root to the queue
    q.append(root)                            
    size=size+1 
    
    # Starting from the second element
    i=1                                       
    while(size>0 and i<len(ip)):
        # Get and remove the front of the queue
        currNode=q[0]
        q.popleft()
        size=size-1
        
        # Get the current node's value from the string
        currVal=ip[i]
        
        # If the left child is not null
        if(currVal!="N"):
            
            # Create the left child for the current node
            currNode.left=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.left)
            size=size+1
        # For the right child
        i=i+1
        if(i>=len(ip)):
            break
        currVal=ip[i]
        
        # If the right child is not null
        if(currVal!="N"):
            
            # Create the right child for the current node
            currNode.right=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.right)
            size=size+1
        i=i+1
    return root
    
    
if __name__=="__main__":
    t=int(input()) 
    import sys
    sys.setrecursionlimit(10000)
    for _ in range(0,t):
        s=input()
        root=buildTree(s)
        res = Solution().verticalOrder(root)
        for i in res:
            print (i, end=" ")
        print()



# } Driver Code Ends