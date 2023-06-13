#User function Template for python3


class Solution:
	
	def findMaxSum(self,arr, n):
		# code here
		dp = [0 for j in range(n)]
		def solve(arr, n):
		    dp[0] = arr[0]
		    dp[1] = arr[0] + arr[1]
		    dp[2] = max(dp[1], max(arr[0] + arr[2], arr[1] + arr[2]))
		    for i in range(3, n + 1):
		        dp[i] = max(dp[i - 1], max(dp[i - 2] + arr[i], dp[i - 3] + arr[i] + arr[i - 1]))
		    return dp[n]
		res = solve(arr, len(arr) - 1)
	    return res


#{ 
 # Driver Code Starts
#Initial Template for Python 3




if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.findMaxSum(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends