# cracking the coding interview 

# solution 2.2
# return Kth to Last

Class Node():
    def __init__(self,data):
        self.data = data
        self.next = None

# we can use a runner and striker
def return_kth_to_last(self,k):
    runner = self.head
    striker = self.head
    count = 1
    while runner and count != k:
        count += 1 
        runner = runner.next
    while runner.next:
        runner = runner.next
        striker = striker.next
    return striker
# O(n) Time.     O(1)  Space