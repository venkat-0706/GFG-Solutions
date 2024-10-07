#User function Template for python3

class Solution:
    def lps(self, str):
        # code here
        n = len(str)
        lps  = [0] * n
        length = 0
        for i in range(1,n):
            while length > 0 and str[i] != str[length] :
                length = lps[length - 1]
            if str[i] ==  str[length]:
                length += 1
            lps[i] =  length
        return lps[-1]



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        s = input()

        ob = Solution()
        answer = ob.lps(s)
        print(answer)

# } Driver Code Ends