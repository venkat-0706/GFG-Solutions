class Solution:
	def countPairsWithDiffK(self,arr, k):
	    count = 0
	    hashMap = {}
    	for i in arr:
    	    hashMap[i] = hashMap.get(i, 0) + 1
    	   
    	for number in arr:
    	    c = number + k
    	    if c in hashMap:
    	        count += hashMap[c]
    	return count


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        k = int(input().strip())
        ob = Solution()
        ans = ob.countPairsWithDiffK(arr, k)
        print(ans)
        print("~")
        tc -= 1

# } Driver Code Ends