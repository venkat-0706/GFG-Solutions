#User function Template for python3

class Solution:
    def minRepeats(self, s1, s2):
        ss1 = set(s1)
        ss2 = set(s2)
        
        for k in ss2:
            if k not in ss1:
                return -1
                
        count = 1
        c = len(s2)
        new_s1 = s1
        
        # rounds
        while len(new_s1) <= 2*c:
            if new_s1.find(s2) != -1:
                return count
            count += 1
            new_s1 += s1
            
        # one extra round
        if new_s1.find(s2) != -1:
                return count
            
        return -1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        A = input()
        B = input()

        ob = Solution()
        print(ob.minRepeats(A, B))

# } Driver Code Ends