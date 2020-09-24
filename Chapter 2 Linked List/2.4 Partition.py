# cracking the coding interview 

# solution 2.4
# partiton list
def partition(head, x):
	small_head = None
	small_tail = None
	large_head = None
	large_tail = None
	cur = head
	while cur:
		if cur.data < x:
			if small_head is None:
				small_head = cur
				small_tail = small_head
			else:
				small_tail.next =  cur
				small_tail = cur
		else:
			if large_head is None:
				large_head = cur
				large_tail = large_head
			else:	
				large_tail.next = cur
				large_tail = cur
				
	cur = cur.next
	# if there is no lesser element in the list => important corner case
	if small_tail is None:
		return large_head
	small_tail.next = large_head
	return small_head 