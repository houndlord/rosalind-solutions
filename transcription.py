def transcription(data):
    print(data.replace('T', 'U'))

with open('./files/rosalind_rna.txt') as f:
    data = f.read()
transcription(data)