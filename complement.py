def complement(data):
    res = ''
    for i in data:
        if i == 'A':
          res += 'T'
        if i == 'C':
          res += 'G'
        if i == 'T':
          res += 'A'
        if i == 'G':
          res += 'C'
    return res

with open('./files/rosalind_revc.txt') as f:
    data = f.read()
print(complement(data))