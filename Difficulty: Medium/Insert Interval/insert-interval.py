#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
     def insertInterval(self, intervals, newInterval):
        # Code here
        def merge(i1, i2):
            if i2[0] < i1[0]:
                i1, i2 = i2, i1
            if i1[1] < i2[0]:
                return i1, i2
            return None, (min(i1[0], i2[0]), max(i1[1], i2[1]))
            
        res = []
        for i in intervals:
            into, newInterval = merge(i, newInterval)
            if into:
                res.append(into)
                
        res.append(newInterval)
        return res
        
        # Code here

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        N = int(input())
        intervals = [list(map(int, input().split())) for i in range(N)]
        newEvent = list(map(int, input().split()))
        ob = Solution()
        res = ob.insertInterval(intervals, newEvent)
        print('[', end = '')
        for i in range(len(res)):
            print('[', end = '')
            print(str(res[i][0])+','+str(res[i][1]), end = '')
            print(']', end = '')
            if i < len(res)-1:
                print(',', end='')
        print(']')
        print("~")
# } Driver Code Ends