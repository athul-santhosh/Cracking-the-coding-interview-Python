# cracking the coding interview 

# solution 2.6
# palindrome or not

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None

    def append(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node=self.head
        while last_node.next:
            last_node=last_node.next
        last_node.next=new_node

    def palindrome(self):
        fast = self.head
        slow = self.head
        stack = []

        # find the middle element of the list 

        while fast and fast.next:
            fast = fast.next.next
            stack.append(slow.data)
            slow = slow.next
        # if the list is of odd length then , slow would be pointing to the exact middle 
        #and fast would be at the last element
        # if thats the case , increment slow by one

        if fast:
            slow = slow.next
        while slow:
            elem = stack.pop()
            if elem != slow.data:
                return False
            slow = slow.next
        if len(stack)== 0:
            return True








athullist=LinkedList()
athullist.append(2)
athullist.append(5)
athullist.append(67)
athullist.append(5)
athullist.append(2)
print(athullist.palindrome())