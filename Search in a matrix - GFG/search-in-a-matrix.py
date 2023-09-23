#User function Template for python3
class Solution:
	def matSearch(self,matrix, N, M, target):
		# Complete this function
        l, r = 0, len(matrix[0]) - 1
        
        while l < len(matrix) and r >= 0:
            if matrix[l][r] < target:
                l += 1
            elif matrix[l][r] > target:
                r -= 1
            else:
                return 1
        return 0

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        
        arr = [int(x) for x in input().split()]
        x = int(input())
        mat = [[0 for j in range(m)] for i in range(n)]
        
        for i in range(n):
            for j in range(m):
                mat[i][j] = arr[i * m + j]
        ob = Solution()
        print(ob.matSearch(mat, n, m, x))
# } Driver Code Ends