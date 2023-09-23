#User function Template for python3

class Solution:
    def findMin(self, arr, n):
        #complete the function here
        l, r = 0, len(arr) - 1
        while l < r:
            mid = l + (r - l) // 2
            if arr[mid] > arr[r]:
                l = mid + 1
            else:
                r = mid
        return min(arr[l], arr[r])

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = [int(x) for x in input().split()]
        ob = Solution()
        print(ob.findMin(arr, n))
# } Driver Code Ends