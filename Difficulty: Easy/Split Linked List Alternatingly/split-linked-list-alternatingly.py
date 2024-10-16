#User function Template for python3
'''
class Node:
    def _init_(self, data):
        self.data = data
        self.next = None

'''
class Solution:
    def alternatingSplitList(self, head):
        dummy=[Node(None),Node(None)]
        odd=0
        cur=head
        dum=[dummy[0],dummy[1]]
        while cur:
            dum[odd].next=cur
            dum[odd]=dum[odd].next
            odd=(odd+1)%2
            cur=cur.next
        dum[0].next=None
        dum[1].next=None
        dummy[0]=dummy[0].next
        dummy[1]=dummy[1].next
        return dummy
        


#{ 
 # Driver Code Starts
class Node:

    def __init__(self, x):
        self.data = x
        self.next = None


def printList(node):
    while node is not None:
        print(node.data, end=" ")
        node = node.next
    print()


if __name__ == "__main__":
    t = int(input().strip())

    for _ in range(t):
        arr = list(map(int, input().strip().split()))

        head = Node(arr[0])
        tail = head

        for i in range(1, len(arr)):
            tail.next = Node(arr[i])
            tail = tail.next

        ob = Solution()
        result = ob.alternatingSplitList(head)
        printList(result[0])
        printList(result[1])

# } Driver Code Ends