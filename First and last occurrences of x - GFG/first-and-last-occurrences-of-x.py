#User function Template for python3


class Solution:
    def find(self, arr, n, x):
        
        # code here
        def findFirst(nums, target):
            l, r = 0, len(nums)
            while l < r:
                mid = l + (r - l) // 2
                if nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid
            if l < len(nums) and nums[l] == target:
                return l
            return -1
        
        def findLast(nums, target):
            l, r = 0, len(nums)
            while l < r:
                mid = l + (r - l) // 2
                if nums[mid] <= target:
                    l = mid + 1
                else:
                    r = mid
            if r > 0 and nums[r - 1] == target:
                return r - 1
            return -1
        
        res = [0] * 2
        res[0] = findFirst(arr, x)
        res[1] = findLast(arr, x)
        return res


#{ 
 # Driver Code Starts
t=int(input())
for _ in range(0,t):
    l=list(map(int,input().split()))
    n=l[0]
    x=l[1]
    arr=list(map(int,input().split()))
    ob = Solution()
    ans=ob.find(arr,n,x)
    print(*ans)
# } Driver Code Ends