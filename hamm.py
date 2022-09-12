def hamm(s1, s2):
    dist = 0
    for i in range(0, len(s1)):
        if s1[i] != s2[i]:
            dist += 1
    return dist


with open('./files/hamm.txt') as f:
    print(hamm(f.readline(), f.readline()))