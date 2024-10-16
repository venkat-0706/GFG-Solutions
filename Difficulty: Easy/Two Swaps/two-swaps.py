class Solution:
    def checkSorted(self, arr):
        #code here
        swaps = 0
        for i, e in enumerate(arr):
            while e-1 != i:
                t = arr[e-1]
                arr[e-1] = e
                e = t
                swaps += 1
        return swaps == 2 or swaps == 0


#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input().strip())

    for _ in range(t):
        arr = list(map(int, input().split()))

        sol = Solution()
        result = sol.checkSorted(arr)
        if result:
            print("true")
        else:
            print("false")

# } Driver Code Ends