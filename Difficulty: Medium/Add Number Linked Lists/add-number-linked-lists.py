#User function Template for python3

''' Node for linked list:

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''
class Solution:
    
    def reverse(self, head):
        p = None
        c = head
        t = c.next
        while c:
            t = c.next
            c.next = p
            p = c
            c = t
        return p
    
    def insertAtEnd(self, h, t, node):
        # When we have empty linked list
        if not(h and t):
            # print("First insertion")
            h = node
            t = node
        # When we have elements in the linked list
        else:
            # print('New Insertion',t.data)
            t.next = node
            t = node
        return h,t
    
    def add(self, p1, p2):
        carry = 0
        head = tail = None
        while p1 or p2 or carry!=0:
            val1 = 0
            if p1:
                val1 = p1.data
            
            val2 = 0
            if p2:
                val2 = p2.data
            
            s = carry + val1 + val2
            
            digit = s%10
            # Create new node for current place's digit
            new_node = Node(digit)
            # Attach this new_node to answer in the end
            head, tail = self.insertAtEnd(head,tail,new_node)
            # Fetch carry
            carry = s//10
            
            if p1:
                p1 = p1.next
            
            if p2:
                p2 = p2.next
            
        # while p1 and p2:
        #     s = carry + p1.data + p2.data
        #     digit = s%10
        #     # Create new node for current place's digit
        #     new_node = Node(digit)
        #     # Attach this new_node to answer in the end
        #     head, tail = self.insertAtEnd(head,tail,new_node)
        #     # Fetch carry
        #     carry = s//10
            
        #     p1=p1.next
        #     p2=p2.next
        
        # while p1:
        #     s = carry + p1.data
        #     digit = s%10
        #     # Create new node for current place's digit
        #     new_node = Node(digit)
        #     # Attach this new_node to answer in the end
        #     head, tail = self.insertAtEnd(head,tail,new_node)
        #     # Fetch carry
        #     carry = s//10
        #     p1 = p1.next
            
        # while p2:
        #     s = carry + p2.data
        #     digit = s%10
        #     # Create new node for current place's digit
        #     new_node = Node(digit)
        #     # Attach this new_node to answer in the end
        #     head, tail = self.insertAtEnd(head,tail,new_node)
        #     # Fetch carry
        #     carry = s//10
        #     p2 = p2.next
        
        # while carry:
        #     s = carry
        #     digit = s%10
        #     # Create new node for current place's digit
        #     new_node = Node(digit)
        #     # Attach this new_node to answer in the end
        #     head, tail = self.insertAtEnd(head,tail,new_node)
        #     # Fetch carry
        #     carry = s//10
        
        return head
        
            
    
    #Function to add two numbers represented by linked list.
    def addTwoLists(self, num1, num2):
        # code here
        
        # s-1 reversing the list
        num1 = self.reverse(num1)
        num2 = self.reverse(num2)
        
        # s-2 adding
        ans = self.add(num1, num2)
        
        
        # return head of sum list
        return self.reverse(ans)


#{ 
 # Driver Code Starts
#Initial Template for Python 3


# Node Class
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


# Linked List Class
class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    # creates a new node with given value and appends it at the end of the linked list
    def insert(self, val):
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next


# prints the elements of linked list starting with head
def printList(n):
    while n:
        print(n.data, end=' ')
        n = n.next
    print()


if __name__ == '__main__':
    for _ in range(int(input())):

        arr1 = (int(x) for x in input().split())
        num1 = LinkedList()
        for i in arr1:
            num1.insert(i)

        arr2 = (int(x) for x in input().split())
        num2 = LinkedList()
        for i in arr2:
            num2.insert(i)

        res = Solution().addTwoLists(num1.head, num2.head)
        printList(res)

# } Driver Code Ends