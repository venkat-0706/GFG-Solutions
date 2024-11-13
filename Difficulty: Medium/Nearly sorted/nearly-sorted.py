

class Solution:
    def nearlySorted(self, arr, k):
        import heapq
        hp=[]
        for ix,ve in enumerate(arr):
            heapq.heappush(hp,ve)
            if ix>=k:
                arr[ix-k]=heapq.heappop(hp)
        for ix in range(k):
            arr[-k+ix]=heapq.heappop(hp)

#{ 
 # Driver Code Starts
# Initial Template for Python 3
# Position this line where user code will be pasted.
# Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        k = int(input())
        ob = Solution()
        ob.nearlySorted(arr, k)
        print(*arr)
        print("~")
        t -= 1
# } Driver Code Ends