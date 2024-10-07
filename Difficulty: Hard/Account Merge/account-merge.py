#User function Template for python3

class Solution:
    def accountsMerge(self, accounts):
        
        def find_parent(n):
            
            if parent[n] == n:
                return n
            parent[n] = find_parent(parent[n])
            return parent[n]
            
            
        def disjoint(n1 , n2):
            
            p1, p2 = find_parent(n1), find_parent(n2)
            if p1 == p2:
                return
            if rank[p1] > rank[p2]:
                parent[p2] = p1
            elif rank[p2] > rank[p1]:
                parent[p1] = p2
            else:
                parent[p1] = p2
                rank[p2] += 1
        
        n = len(accounts)
        parent = [i for i in range(n)]
        rank = [0 for i in range(n)]
        e_to_node = {}
        
        for i, a in enumerate(accounts):
            for e in a[1:]:
                if e in e_to_node:
                    disjoint(i, e_to_node[e])
                else:
                    e_to_node[e] = i
        
        merged_a = [[] for i in range(n)]
        for email, no in e_to_node.items():
            merged_a[find_parent(no)].append(email)
        #print(merged_a)
        for a in merged_a:
            a.sort()
        for i in range(n):
            #print(i,n, accounts[i])
            if merged_a[i]:
                merged_a[i].insert(0, accounts[i][0])
        merged_a = list(filter(None, merged_a))
        return merged_a
            
            

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        n = int(input())
        accounts = []
        for i in range(n):
            cntEmails = int(input())
            nameEmails = input().split()
            accounts.append(nameEmails)
        ob = Solution()
        res = ob.accountsMerge(accounts)
        res.sort()
        print('[', end = '')
        for i in range(len(res)):
            print('[', end = '')
            for j in range(len(res[i])):
                if j != (len(res[i]) - 1):
                    print(res[i][j], end = ', ')
                else:
                    print(res[i][j], end='')
            if (i != len(res) - 1):
                print('], ')
            else:
                print(']', end = '')
        print(']')
# } Driver Code Ends