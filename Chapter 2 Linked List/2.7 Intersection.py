# cracking the coding interview 

# solution 2.7
# intersection of two nodes

"""class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
"""
def intersection(headA,headB):
    dict = {} 
    while headA:
        dict[headA] = 1
        headA = headA.next
    # checking wehter any node of first linked list is in second one
    while headB:
        if headB in dict:
            return headB
        else:
            headB = headB.next
    return None
