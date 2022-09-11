def count(data):
    a, c, g, t  = 0, 0, 0, 0
    for i in data:
        if i == 'A':
            a += 1
        if i == 'G':
            g += 1
        if i == 'C':
            c += 1
        if i == 'T':
            t += 1
    print(a, c, g, t, sep=' ')
    #print(str(a) + ' ' + str(c) + ' ' + str(g) + ' ' + str(t))


with open('./files/rosalind_dna.txt') as f:
    data = f.read()
count(data)
