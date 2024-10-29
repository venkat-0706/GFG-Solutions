def quickSort(head):
    #return head after sorting
    
    def sort(h, t):
        if not h or h == t or h.next == t:
            return h
            
        v = h.data
        dummy = Node(0)
        dummy.next = h
        
        prev, w = dummy, h
        
        while w != t:
            nw = w.next
            if w.data < v:
                prev.next = w.next
                w.next = dummy.next
                dummy.next = w
            else:
                prev = prev.next
                
            w = nw
        
        h.next = sort(h.next, t)
        return sort(dummy.next, h)
    return sort(head, None)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
from collections import defaultdict


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class Llist:

    def __init__(self):
        self.head = None

    def insert(self, data, tail):
        node = Node(data)

        if not self.head:
            self.head = node
            return node

        tail.next = node
        return node


def nodeID(head, dic):
    while head:
        dic[head.data].append(id(head))
        head = head.next


def printList(head, dic):
    while head:
        if id(head) not in dic[head.data]:
            print("Do'nt swap data, swap pointer/node")
            return
        print(head.data, end=' ')
        head = head.next


if __name__ == '__main__':
    t = int(input())

    for tcs in range(t):

        arr = [int(x) for x in input().split()]

        ll = Llist()
        tail = None

        for nodeData in arr:
            tail = ll.insert(nodeData, tail)

        dic = defaultdict(list)  # dictonary to keep data and id of node
        nodeID(ll.head, dic)  # putting data and its id

        resHead = quickSort(ll.head)
        printList(resHead, dic)  #verifying and printing
        print()

        print("~")

# } Driver Code Ends