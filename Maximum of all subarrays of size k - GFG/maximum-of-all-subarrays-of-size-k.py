#User function Template for python3

class Solution:
    
    #Function to find maximum of each subarray of size k.
    def max_of_subarrays(self,arr,n,k):
        
        res = []
        q = deque()
    
        i = 0
        j = 0
    
        while j < len(arr):
            while q and arr[j] >= arr[q[-1]]:
                q.pop()
            q.append(j)
            
            if j - i + 1 < k:
                j += 1
            elif j - i + 1 == k:
                res.append(arr[q[0]])
                if q[0] == i:
                    q.popleft()
                j += 1
                i +=1 
        return res

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys
from collections import deque

#Contributed by : Nagendra Jha

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n,k = map(int,input().strip().split())
        arr = list(map(int,input().strip().split()))
        ob=Solution()
        res = ob.max_of_subarrays(arr,n,k)
        for i in range (len (res)):
            print (res[i], end = " ")
        print()
# } Driver Code Ends