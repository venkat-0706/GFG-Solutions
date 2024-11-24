#User function Template for python3
class Solution:

	# Function to find maximum
	# product subarray
	def maxProduct(self,arr):
	    n = len(arr)
        if n < 2:
            return arr[0]
        prefix_product = 1
        suffix_product = 1
        max_product = float('-inf')
        for i in range(n):
            if prefix_product == 0:
                prefix_product = 1
            if suffix_product == 0:
                suffix_product = 1
            prefix_product *= arr[i]
            suffix_product *= arr[n-1-i]
            max_product = max(max_product, prefix_product, suffix_product)
        return max_product
		# code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.maxProduct(arr)
        print(ans)
        tc -= 1

# } Driver Code Ends