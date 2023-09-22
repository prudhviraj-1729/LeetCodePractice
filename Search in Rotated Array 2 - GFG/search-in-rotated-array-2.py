#User function Template for python3

class Solution:
    def Search(self, n, arr, k):
        # code here
        l, r = 0, len(arr)
        while l < r:
            mid = l + (r - l) // 2
            if arr[mid] == k:
                return 1
            if arr[l] == arr[mid]:
                l += 1
                continue
            elif arr[l] < arr[mid]:
                if k < arr[l] or k > arr[mid]:
                    l = mid + 1
                else:
                    r = mid
            else:
                if k > arr[r - 1] or k < arr[mid]:
                    r = mid 
                else:
                    l = mid + 1
        return 0

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        k = int(input())
        ob = Solution()
        ans = ob.Search(n, arr, k)
        print(ans)
        tc -= 1
# } Driver Code Ends