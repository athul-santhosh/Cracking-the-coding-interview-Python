# cracking the coding interview 

# solution 1.6
#String Comprehension

def string_compression1(s):                          # this solution can be effective if we dont have an alphabet  
    s_dict ={}                                       # is not repeated
    for i in s:
        if i in s_dict:
            s_dict[i] += 1
        else:
            s_dict[i] = 1
    print(s_dict)
    s_comp = ""
    for alpha,value in s_dict.items():
        s_comp += str(alpha)+str(value)
    print(s_comp)

#string_compression1("aabcccccaaa")

# thinking for alternate solution
def string_compression2(s):
    string_comp = ""
    count_consecutive = 0
    for i in range(len(s)):
        count_consecutive += 1
        if i+1>= len(s) or s[i] != s[i+1]:
            string_comp += str(s[i]) + str(count_consecutive)
            count_consecutive = 0                                # Important Note, we can set value to desired  at the end 
                                                                 # of for loop
        if len(s) < len(string_comp):                            # follow up case given in question
            return s
    return string_comp

        

print(string_compression2("abcdefgh"))
