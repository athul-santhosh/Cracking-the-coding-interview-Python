# cracking the coding interview 

# solution 1.4
#Palindrome Permutation

# approach  we create a dict ,we iterate through dict, if we get count 
# greater than 1 ,we return false else true

def palindrome_permutation(p): 
	p = p.lower().replace(" ","")        		 # avoiding whitespace and case sensitivity

	# print(p)
	P_dict = dict()                     		 #count all the occurences of each alphabet with dictionary
	for i in p:
		if i in P_dict:
			P_dict[i] += 1
		else:
			P_dict[i] = 1
	# print(P_dict)
	count = 0
	for value,occurence in P_dict.items():        #checks for the occurences of eachitem wether its even  or odd
		if occurence % 2 == 0:
			count += 0
		else:                                      
			count += 1
	# print(count)
	if count > 1:                                 # if there is a single odd then ,we can still form a palindrome
		return false                              # with odd count element on the middle
	return True

print(palindrome_permutation("Racecar"))
