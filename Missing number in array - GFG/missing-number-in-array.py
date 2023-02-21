#User function Template for python3


class Solution:
    def MissingNumber(self,array,n):
        # code here
        sum = (n * (n + 1)) / 2
        arraysum = 0
        for i in range(len(array)):
            arraysum += array[i]
        return int(sum - arraysum)

#{ 
 # Driver Code Starts
#Initial Template for Python 3




t=int(input())
for _ in range(0,t):
    n=int(input())
    a=list(map(int,input().split()))
    s=Solution().MissingNumber(a,n)
    print(s)
# } Driver Code Ends