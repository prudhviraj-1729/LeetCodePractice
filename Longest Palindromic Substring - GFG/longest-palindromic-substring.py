#User function Template for python3

class Solution:
    def longestPalindrome(self, s):
        # code here
        def f(s, l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l + 1: r]
        
        p = ""
        for i in range(len(s)):
            p1 = f(s, i, i)
            p2 = f(s, i, i + 1)
            p = max(p, p1, p2, key=len)
        return p


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        
        S = input().strip()
        ob=Solution()
        print(ob.longestPalindrome(S))
# } Driver Code Ends