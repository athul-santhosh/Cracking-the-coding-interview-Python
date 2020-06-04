# cracking the coding interview 

# solution 1.2
#palindrome permutation

#naive

def is_permutation(s,p):              # using sorted function time: O(n log n) space :O(1)
    if len(s) != len(p):
        return False
    s=sorted(s)
    p=sorted(p)
    print(s)
    print(p)
    return s == p


def is_p_dict(s,p):                   # using dictionary time O(n) space: O(n)
    if len(s) != len(p):
        return False
    return _is_p_dict(s) == _is_p_dict(p)

def _is_p_dict(c):
    permutation = {}
    for i in c:
        if i in permutation:
            permutation[i] += 1
        else:
            permutation[i] = 1
    return permutation


print(is_p_dict("mood","doom"))