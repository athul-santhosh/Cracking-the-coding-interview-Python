# cracking the coding interview 

# solution 2.1
# remove dups 

Class Node():
    def __init__(self,data):
        self.data = data
        self.next = None


def remove_duplicate(self):
    taken = {}
    current = self.head
    while current:
        if current.data not in taken:
            taken[current.data] = 1
            prev = current
        else:
            prev.next = current.next
        current = current.next

# O(n) Time O(n) space

# what if temporary buffer is not allowed

def remove_duplicate_(self):
    cur = self.head
    while cur:
        runner=cur
        while runner.next:
            if runner.next == runner.next.data:
                runner.next = runner.next.next
            else:
                runner.next
        cur = cur.next

# O(n^2) Time    O(1) space
