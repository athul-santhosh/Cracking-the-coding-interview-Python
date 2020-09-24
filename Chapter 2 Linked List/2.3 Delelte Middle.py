# cracking the coding interview 

# solution 2.3
# Delete the middle node

Class Node():
    def __init__(self,data):
        self.data = data
        self.next = None

# we can use a runner and striker
def deleteMiddle(self,n):
    if n is None or n.next is None:
        print("Invalid Node")
    temp = n.next
    n.data = temp.data
    n.next = temp.next
    temp = None




# O(1) Time.     O(1)  Space