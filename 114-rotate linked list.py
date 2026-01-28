#rotate linked list problem
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def rotate_right(head, k):
    if not head or k == 0:
        return head

    # Compute the length of the list and get the tail node
    length = 1
    tail = head
    while tail.next:
        tail = tail.next
        length += 1

    # Make the list circular
    tail.next = head

    # Find the new tail: (length - k % length - 1)th node
    # and the new head: (length - k % length)th node
    k = k % length
    new_tail = head
    for _ in range(length - k - 1):
        new_tail = new_tail.next
    new_head = new_tail.next

    # Break the circle
    new_tail.next = None

    return new_head
# Example usage
def print_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

# Example usage
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
k = 2
rotated_head = rotate_right(head, k)
print_list(rotated_head)  # Output: 4 -> 5 -> 1 -> 2 -> 3 -> None