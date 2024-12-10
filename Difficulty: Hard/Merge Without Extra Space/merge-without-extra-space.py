class Solution:
    def mergeArrays(self, a, b):
        i=len(a)-1
        j=0
        while i>=0 and j<len(b):
            if a[i]>b[j]:
                a[i],b[j]=b[j],a[i]
                i-=1
                j+=1
            else:
                break
        a.sort()
        b.sort()


#{ 
 # Driver Code Starts
# Input handling and main function
if __name__ == "__main__":
    # Number of test cases
    t = int(input().strip())

    for _ in range(t):
        # Input first array
        a = list(map(int, input().strip().split()))
        # Input second array
        b = list(map(int, input().strip().split()))

        # Create solution object and merge the arrays
        solution = Solution()
        solution.mergeArrays(a, b)

        # Output both arrays in the same line space-separated
        print(" ".join(map(str, a)))
        print(" ".join(map(str, b)))

# } Driver Code Ends