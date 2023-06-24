#User function Template for python3
class Solution:
    def maximumSumSubarray (self,k,arr,n):
        # code here 
        i, j = 0, 0
        total = 0
        res = 0
        
        while j < len(arr):
            total += arr[j]
            if j - i + 1 < k:
                j += 1
            elif j - i + 1 == k:
                res = max(res, total)
                total = total - arr[i]
                i += 1
                j += 1
        return res
                


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        
        N,K = input().split()
        N = int(N)
        K = int(K)
        Arr = list( map(int,input().strip().split(" ")))

        ob = Solution()
        print(ob.maximumSumSubarray(K,Arr,N))
# } Driver Code Ends