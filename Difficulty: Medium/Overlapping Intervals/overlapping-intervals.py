class Solution:
    	def mergeOverlap(self, arr):
            arr.sort()
            output = []
            curr_start, curr_end = arr[0]
            for start, end in arr:
                if start <= curr_end:
                    curr_end = max(curr_end, end)
                else:
                    output.append((curr_start, curr_end))
                    curr_start, curr_end = start, end
            output.append((curr_start, curr_end))
            return output


#{ 
 # Driver Code Starts
if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n = int(input())
        # a = list(map(int, input().strip().split()))
        arr = []
        # j = 0
        for i in range(n):
            a = list(map(int, input().strip().split()))
            x = a[0]
            # j += 1
            y = a[1]
            # j += 1
            arr.append([x, y])
        obj = Solution()
        ans = obj.mergeOverlap(arr)
        for i in ans:
            for j in i:
                print(j, end=" ")
        print()

# } Driver Code Ends