#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def subArraySum(self,arr, target):
        ans = ssum = 0
        d = dict()
        d[0] = 1
        for idx, item in enumerate(arr):
            ssum += item
            if ssum - target in d:
                ans += d[ssum - target]
            d[ssum] = d.get(ssum, 0) + 1
        return ans

#{ 
 # Driver Code Starts.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        tar= int(input())
        ob = Solution()
        res = ob.subArraySum(arr,tar)
        print(res)
        # print("~")
        t -= 1


# } Driver Code Ends