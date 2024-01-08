def is_anagram(s1, s2):
    if len(s1) != len(s2):
        return False
    s1 = sorted(s1)
    s2 = sorted(s2)
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            return False
    return True

def is_anagram_sorted(s1, s2):
    pass


print(is_anagram("listen", "silent"))