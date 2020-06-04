# cracking the coding interview 

# solution 1.3
#URLify
def replace_char(s):                  # can be solved using replace built in method
	s = s.replace(" ","%20")
	return s

print(replace_char("athul is strong "))