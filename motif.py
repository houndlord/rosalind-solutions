def motif(s1, s2):
    res = []
    i = len(s2)
    j = 0
    while i != len(s1):
        if s1[j:i] == s2:
            res.append(j+1)
        i = i+1
        j = j+1
    return res

with open('./files/motif.txt') as f:
    print(motif(f.readline(), f.readline()))