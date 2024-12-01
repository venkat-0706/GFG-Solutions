

class Solution:
    def search(self, pat, txt):
        def computeLPSArray(pat):
            lps = [0] * len(pat)
            length = 0 
            i = 1
            while i < len(pat):
                if pat[i] == pat[length]:
                    length += 1
                    lps[i] = length
                    i += 1
                else:
                    if length != 0:
                        length = lps[length - 1]
                    else:
                        lps[i] = 0
                        i += 1
            return lps
        
        m = len(pat)
        n = len(txt)
        lps = computeLPSArray(pat)
        
        i = 0  
        j = 0  
        result = []

        while i < n:
            if pat[j] == txt[i]:
                i += 1
                j += 1
            
            if j == m:
                result.append(i - j) 
                j = lps[j - 1]
            elif i < n and pat[j] != txt[i]:
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1

        return result
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input().strip()
        patt = input().strip()
        ob = Solution()
        ans = ob.search(patt, s)
        if len(ans) == 0:
            print("[]", end="")
        for value in ans:
            print(value, end=' ')
        print()

# } Driver Code Ends