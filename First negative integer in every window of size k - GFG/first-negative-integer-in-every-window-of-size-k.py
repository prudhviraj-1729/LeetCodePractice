#User function Template for python3
from collections import deque

def printFirstNegativeInteger( arr, n, k):
    # code here
            
    q = deque()
    i, j = 0, 0
    res = []
    
    while j < len(arr):
        if arr[j] < 0:
            q.append(arr[j])
        if j - i + 1 < k:
            j += 1
        elif j - i + 1 == k:
            if len(q) == 0:
                res.append(0)
            else:
                res.append(q[0])
                if q[0] == arr[i]:
                    q.popleft()
            i += 1
            j += 1
            
    return res

#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        k = int(input())
        
        answer = printFirstNegativeInteger(a, n, k)
        for i in answer:
            print(i,end=" ")
        print()

        T -= 1


if __name__ == "__main__":
    main()


# } Driver Code Ends