class Solution:
    def editDistance(self, str1, str2):
        m=len(str1)
        n=len(str2)
        from functools import lru_cache
        @lru_cache(None)
        def dfs(i=m-1,j=n-1):
            nonlocal str1,str2
            if i<0 and j<0:
                return 0
            if i<0 or j<0:
                return max(i,j)+1
            if str1[i]==str2[j]:
                return dfs(i-1,j-1)
            return min(dfs(i-1,j),dfs(i,j-1),dfs(i-1,j-1))+1
        return dfs()
		# Code here


#{ 
 # Driver Code Starts
if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        s, t = input().split()
        ob = Solution()
        ans = ob.editDistance(s, t)
        print(ans)

# } Driver Code Ends