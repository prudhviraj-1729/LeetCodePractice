#User function Template for python3

class Solution:
    
    #Function to find maximum of each subarray of size k.
    def max_of_subarrays(self,arr,n,k):
        
        res = []
        q = []

    # Process the first k elements
        for i in range(k):
        # Remove indices of elements smaller than the current element from the right end of the list
            while q and arr[i] > arr[q[-1]]:
                q.pop()
            q.append(i)

    # Process the remaining elements
        for i in range(k, len(arr)):
            # The front element of the list is the maximum for the current window
            res.append(arr[q[0]])
    
            # Remove indices of elements from the front of the list that are outside the current window
            if q[0] == i - k:
                q.pop(0)
    
            # Remove indices of elements smaller than the current element from the right end of the list
            while q and arr[i] > arr[q[-1]]:
                q.pop()
    
            q.append(i)
    
        # Add the maximum for the last window
        res.append(arr[q[0]])
    
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