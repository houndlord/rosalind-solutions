def transcription(data):
    print(data.replace('T', 'U'))

with open('./rosalind_rna.txt') as f:
    data = f.read()
transcription(data)