# cracking the coding interview 

# solution 2.8
#  Loop Detection

"""class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
"""
def loop_element(self):
    slow = self.head
    fast = self.head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    #if no cylce exist then this condition goes true
    if fast == None or fast.next == None:
        return None
    striker = self.head
    while striker != fast:
        striker = striker.next
        fast = fast.next
    return striker
