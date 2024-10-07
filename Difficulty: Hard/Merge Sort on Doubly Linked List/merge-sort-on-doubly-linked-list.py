class Solution:

    def merge(self, first, second):
        if first is None:
            return second
        if second is None:
            return first

        if first.data < second.data:
            first.next = self.merge(first.next, second)
            if first.next:  # Ensure first.next is not None before accessing its prev
                first.next.prev = first
            first.prev = None
            return first
        else:
            second.next = self.merge(first, second.next)
            if second.next:  # Ensure second.next is not None before accessing its prev
                second.next.prev = second
            second.prev = None
            return second

    def split_list(self, head):
        if head is None or head.next is None:
            return None

        slow, fast = head, head

        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

        temp = slow.next
        slow.next = None
        if temp:
            temp.prev = None
        return temp

    def sort_doubly(self, head):
        if head is None or head.next is None:
            return head

        second = self.split_list(head)
        head = self.sort_doubly(head)
        second = self.sort_doubly(second)

        return self.merge(head, second)


    


#{ 
 # Driver Code Starts
class DLLNode:

    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None


def push(tail_ref, new_data):
    new_node = DLLNode(new_data)
    new_node.next = None
    new_node.prev = tail_ref

    if tail_ref:
        tail_ref.next = new_node

    return new_node


def print_list(head):
    if head is None:
        return

    # Forward traversal
    result_forward = []
    last = None
    while head is not None:
        result_forward.append(str(head.data))
        last = head
        head = head.next

    print(" ".join(result_forward))

    # Backward traversal
    result_backward = []
    while last is not None:
        result_backward.append(str(last.data))
        last = last.prev

    print(" ".join(result_backward))


if __name__ == "__main__":
    t = int(input().strip())
    for _ in range(t):
        arr = list(map(int, input().strip().split()))
        if not arr:
            print("List is empty.")
            continue

        head = DLLNode(arr[0])
        tail = head

        for value in arr[1:]:
            tail = push(tail, value)

        obj = Solution()
        sorted_head = obj.sort_doubly(head)

        print_list(sorted_head)

# } Driver Code Ends