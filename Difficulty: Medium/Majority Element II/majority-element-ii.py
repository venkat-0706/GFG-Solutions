class Solution:
    def findMajority(self, arr):
        dic = {}
        n = len(arr)
        
        # Counting occurrences of each element
        for i in arr:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        
        # Finding elements that appear more than n // 3 times
        ans = []
        for i in dic:
            if dic[i] > n // 3:
                ans.append(i)
        
        ans.sort()  # Sorting the result
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():
    t = int(input().strip())
    for _ in range(t):
        s = input().strip()
        nums = list(map(int, s.split()))
        ob = Solution()
        ans = ob.findMajority(nums)
        if not ans:
            print("[]")
        else:
            print(" ".join(map(str, ans)))


if __name__ == "__main__":
    main()

# } Driver Code Ends