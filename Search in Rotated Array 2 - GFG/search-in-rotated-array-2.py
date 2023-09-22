#User function Template for python3

class Solution:
    def Search(self, n, nums, target):
        # code here
        l, r = 0, len(nums)
        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return 1
            if nums[l] == nums[mid]:
                l += 1
                continue
            elif nums[l] < nums[mid]:
                if target < nums[l] or target > nums[mid]:
                    l = mid + 1
                else:
                    r = mid
            else:
                if target > nums[r - 1] or target < nums[mid]:
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