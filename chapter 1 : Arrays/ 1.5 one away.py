# cracking the coding interview 

# solution 1.5
#palindrome one away

#naive 

def one_away(s_given,s_edit):
    return replace(s_given,s_edit) or insert(s_given,s_edit) or remove(s_given,s_edit)

def insert(s_given,s_edit):
    if len(s_given)+1 != len(s_edit):   
        return False
    for i in s_edit:                    # time O(n) space O(1)
        if i not in s_given:
            return False
    return True

def remove(s_given,s_edit):
    if len(s_given)-1 != len(s_edit):   # time O(n) space O(1)
        return False
    for i in s_edit:
        if i not in s_given:
            return False
    return True

def replace(s_given,s_edit):           #time O(n) space O(1)
    if len(s_given) != len(s_edit):
        return False
    count = 0
    for i in s_given:
        if i not in s_edit:
            count += 1
    if count >1:
        return False                    # time = O(n) + O(n) + O(n) == O(n) ,space = O(1)
    return True

print(one_away("pale","ple"))
print(one_away("pales","pale"))
print(one_away("pale","bale"))
print(one_away("pale","bake"))





