#User function Template for python3

class Solution:
    def search(self, A : list, l : int, r : int, key : int):
        # l: The starting index
        # h: The ending index, you have to search the key in this range
        # Complete this function
        r = r + 1
        while l < r:
            mid = l + (r - l) // 2
            if A[mid] == key:
                return mid
            if A[l] < A[mid]:
                if key < A[l] or key > A[mid]:
                    l = mid + 1
                else:
                    r = mid
            else:
                if key > A[r - 1] or key < A[mid]:
                    r = mid
                else:
                    l = mid + 1
        return -1

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    
    for _ in range(t):
        n = int(input())
        A = [int(x) for x in input().split()]
        k = int(input())
        ob=Solution()
        print(ob.search(A, 0, n - 1, k))
# } Driver Code Ends