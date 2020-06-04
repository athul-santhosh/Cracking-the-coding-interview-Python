# cracking the coding interview 

# solution 1.9
# string rotation

# u are given a substring function

# the main thing to understand here is yx is always a substring of xyxy

def is_rotation(s1,s2):
	if len(s1) == len(s2) and len(s1) > 0:        #we check wehter the rotated string and given string are of
												  # equal length and are greater than zero length
		s1s1 = s1 + s1

		return is_substring(s1s1,s2)
	return False                                   # time : 0(1) space :O(1)
												   # time O(n + n)

def is_substring(x,y):                            #substring function
	return y in x

y = is_rotation("waterbottle","erbottlewat")
print(y)

