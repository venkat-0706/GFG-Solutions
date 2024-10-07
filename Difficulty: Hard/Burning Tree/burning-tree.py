#User function Template for python3
class Solution:

    def minTime(self, root, target):

        def mark_parents(node, parent_map):

            if not node:

                return

            if node.left:

                parent_map[node.left] = node

                mark_parents(node.left, parent_map)

            if node.right:

                parent_map[node.right] = node

                mark_parents(node.right, parent_map)

        def bfs_to_burn_tree(start):

            from collections import deque

            queue = deque([(start, 0)])

            visited = set([start])

            max_time = 0

            while queue:

                node, time = queue.popleft()

                max_time = max(max_time, time)

                if node.left and node.left not in visited:

                    visited.add(node.left)

                    queue.append((node.left, time + 1))

                if node.right and node.right not in visited:

                    visited.add(node.right)

                    queue.append((node.right, time + 1))

                if node in parent_map and parent_map[node] not in visited:

                    visited.add(parent_map[node])

                    queue.append((parent_map[node], time + 1))

            return max_time

        parent_map = {}

        mark_parents(root, parent_map)

        # Locate the target node in the tree

        def find_target(node, target):

            if not node:

                return None

            if node.data == target:

                return node

            left = find_target(node.left, target)

            if left:

                return left

            return find_target(node.right, target)

        target_node = find_target(root, target)

        if not target_node:

            return 0

        return bfs_to_burn_tree(target_node)



#{ 
 # Driver Code Starts
#Initial Template for Python 3

from collections import deque

# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

# Function to Build Tree   
def buildTree(s):
    #Corner Case
    if(len(s)==0 or s[0]=="N"):           
        return None
        
    # Creating list of strings from input 
    # string after spliting by space
    ip=list(map(str,s.split()))
    
    # Create the root of the tree
    root=Node(int(ip[0]))                     
    size=0
    q=deque()
    
    # Push the root to the queue
    q.append(root)                            
    size=size+1 
    
    # Starting from the second element
    i=1                                       
    while(size>0 and i<len(ip)):
        # Get and remove the front of the queue
        currNode=q[0]
        q.popleft()
        size=size-1
        
        # Get the current node's value from the string
        currVal=ip[i]
        
        # If the left child is not null
        if(currVal!="N"):
            
            # Create the left child for the current node
            currNode.left=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.left)
            size=size+1
        # For the right child
        i=i+1
        if(i>=len(ip)):
            break
        currVal=ip[i]
        
        # If the right child is not null
        if(currVal!="N"):
            
            # Create the right child for the current node
            currNode.right=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.right)
            size=size+1
        i=i+1
    return root

if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        line=input()
        target=int(input())
        root=buildTree(line)
        print(Solution().minTime(root,target))

# } Driver Code Ends