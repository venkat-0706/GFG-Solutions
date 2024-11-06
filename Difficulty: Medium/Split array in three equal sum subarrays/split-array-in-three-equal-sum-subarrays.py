#User function Template for python3
class Solution:
    def findSplit(self, arr):

        if sum(arr) % 3:
            return [-1, -1]
            
        target = sum(arr) // 3
        part_visited = 0
        prefix_sum = 0
        first_part_ends_at = -1
        
        for i in range(len(arr)):
            prefix_sum += arr[i]
            
            if prefix_sum == target:
                part_visited += 1
                first_part_ends_at = i
            if prefix_sum == (2*target) and i != len(arr)-1 and part_visited:
                return [first_part_ends_at, i]
                
        return [-1, -1]


#{ 
 # Driver Code Starts
# Initial Template for Python 3

# Main
if __name__ == '__main__':
    t = int(input())
    while t:
        t -= 1
        arr = [int(x) for x in input().strip().split()]

        ob = Solution()
        result = ob.findSplit(arr)

        if result == [-1, -1]:
            print("false")
        else:
            print("true")
        print("~")

# } Driver Code Ends