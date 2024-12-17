
class Solution:
    def findPages(self, arr, k):
        n = len(arr)
        if n < k:
            return -1
        low, high = max(arr), sum(arr)
        while low < high:
            mid = (low + high) // 2
            if Solution.isPossible(arr, k, mid):
                high = mid
            else:
                low = mid + 1
                
        return low

    def isPossible(arr, k, maxPages):
        students, currentSum = 1, 0
        for pages in arr:
            if currentSum + pages > maxPages:
                students += 1
                currentSum = pages
                if students > k:
                    return False
            else:
                currentSum += pages

        return True

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
        ans = ob.findPages(A, D)
        print(ans)
        print("~")

# } Driver Code Ends