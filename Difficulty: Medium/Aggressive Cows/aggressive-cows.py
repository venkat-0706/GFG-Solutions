#User function Template for python3


class Solution:
     def aggressiveCows(self, stalls, k):
        stalls.sort()
        def ok(d, k):
            p = stalls[0]
            for i in range(1, len(stalls)):
                if abs(stalls[i] - p) >= d:
                    p = stalls[i]
                    k -= 1
            return k <= 0
            
        lo, hi = 1, stalls[-1] - stalls[0]
        while lo < hi:
            mi = lo+(hi-lo)//2
            if ok(mi, k-1):
                lo = mi+1
            else:
                hi = mi
        lo -= 1
        return lo



#{ 
 # Driver Code Starts
#Initial Template for Python 3
import bisect
#Main
if __name__ == '__main__':
    t = int(input())
    while t:
        t -= 1
        A = [int(x) for x in input().strip().split()]
        nd = [int(x) for x in input().strip().split()]
        D = nd[0]
        ob = Solution()
        ans = ob.aggressiveCows(A, D)
        print(ans)
        print("~")
# } Driver Code Ends