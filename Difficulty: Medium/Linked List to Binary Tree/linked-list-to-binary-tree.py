
# User function Template for python3

'''
class ListNode:

    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.next = None


# Tree Node structure
class Tree:

    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

'''
from collections import deque
#Function to make binary tree from linked list.
def convert(head):
    root = Tree(head.data)
    q = deque([root])
    temp = head.next
    
    while q:
        node = q.popleft()
        
        if temp:
            node.left = Tree(temp.data)
            temp = temp.next
            q.append(node.left)
            
        if temp:
            node.right = Tree(temp.data)
            temp = temp.next
            q.append(node.right)
            
    return root
    
    # code here


#{ 
 # Driver Code Starts
# Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nikhil Kumar Singh

# Linked List node


class ListNode:

    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.next = None


# Tree Node structure
class Tree:

    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Class to convert the linked list to Binary Tree
class Conversion:
    # Constructor for storing head of linked list
    # and root for the Binary Tree
    def __init__(self, data=None):
        self.head = None
        self.root = None

    def push(self, new_data):

        # Creating a new linked list node and storing data
        new_node = ListNode(new_data)

        # Make next of new node as head
        new_node.next = self.head

        # Move the head to point to new node
        self.head = new_node

    def levelorderTraversal(self, root):
        mylist = []  # reverse list of nodes
        if root is None:
            return
        que = []
        que.append(root)
        while True:
            n = len(que)
            if n == 0:
                break
            while (n > 0):
                node = que.pop(0)
                mylist.append(node.data)
                if node.left is not None:
                    que.append(node.left)
                if node.right is not None:
                    que.append(node.right)
                n -= 1
        mylist = mylist[::-1]
        print(*mylist)
        return


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        a = list(map(int, input().strip().split()))
        mylist = Conversion()  # Create Linked List to be used
        for i in range(n):
            mylist.push(a[i])  # push elements in linked list
        # convert the linked list to binary tree
        root = convert(mylist.head)
        mylist.levelorderTraversal(root)

# } Driver Code Ends