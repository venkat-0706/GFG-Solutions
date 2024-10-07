#User function Template for python3
class Solution:
    def evenlyDivides (self, N):
        k=[int(d) for d in str(N)]
        b=[]
        for i in k:
            if i!=0:
                if N%i==0:
                    b.append(i)
            else:
                None
        return len(b)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
       

        ob = Solution()
        print(ob.evenlyDivides(N))
# } Driver Code Ends