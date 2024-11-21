class Solution:
    def maximumProfit(self, prices):
        n = len(prices)
        if n  < 2:
            return 0
        ans = 0
        run = 0
        for i in range(1,n):
            run = max(0,run + prices[i] - prices[i-1])
            ans = max(ans , run)
        return ans
        # code here


#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())  # Read number of test cases
    for _ in range(t):
        # Read input and split it into a list of integers
        prices = list(map(int, input().split()))
        # Create a Solution object and calculate the result
        obj = Solution()
        result = obj.maximumProfit(prices)
        # Print the result
        print(result)

# } Driver Code Ends