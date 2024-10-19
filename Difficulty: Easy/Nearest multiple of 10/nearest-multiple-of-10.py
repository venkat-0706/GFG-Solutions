#User function Template for python3
sys.set_int_max_str_digits(100000)
class Solution:
    def roundToNearest (self, string) : 
        n=len(string)
        string=int(string)
        left=(string//10)*10
        right=(string//10+1)*10
        if string-left>right-string :
            res=str(right)
        else:
            res=str(left)
        return res.zfill(n)


#{ 
 # Driver Code Starts
#Initial Template for Python 3
for _ in range(0, int(input())):
    num_str = input()
    ob = Solution()
    res = ob.roundToNearest(num_str)
    print(res)

# } Driver Code Ends