import re

def find_uppercase_sequences(text):
    pattern = r'\b[A-Z][a-z]+\b'
    sequences = re.findall(pattern, text)
    return sequences
with open('lab5/row.txt', 'r',encoding='utf-8') as file:
    text = file.read()
    sequences = find_uppercase_sequences(text)
    for sequence in sequences:
                    print(sequence)