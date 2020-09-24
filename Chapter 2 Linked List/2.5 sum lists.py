# cracking the coding interview 

# solution 2.5
# sum list

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def display(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data,end =" --> ")
            cur_node=cur_node.next


    def append(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node=self.head
        while last_node.next:
            last_node=last_node.next
        last_node.next=new_node

    def addtwo(self,l2_head):
        l1 = self.head
        l2 = l2_head
        sumlist = LinkedList()
        carry = 0
        while l1 or l2 or carry:
            sum = 0 
            if l1:
                sum += l1.data
                l1 = l1.next
            if l2:
                sum += l2.data
                l2 = l2.next
            sum += carry
            carry = sum //10  
            sum = sum % 10
            if l1 or l2 or sum:
                sumlist.append(sum)
        sumlist.display()

athullist=LinkedList()
athullist.append(2)
athullist.append(5)
athlist = LinkedList()
athlist.append(4)
athlist.append(9)
athullist.addtwo(athlist.head)






