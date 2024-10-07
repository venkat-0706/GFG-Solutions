#User function Template for python3

class Solution:
    def longestSubstring(self, s , n):
        # code here 
        
       

        ln = len(s)

        res = "-1"

        l = 0

        r = 0

        for r in range(ln):

            substr = s[l:r+1]

            if s.find(substr, r+1) != -1:

                res = substr

            else:

                l+=1


        return res

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        S=input()
        
        ob = Solution()
        print(ob.longestSubstring(S , N))
# } Driver Code Ends