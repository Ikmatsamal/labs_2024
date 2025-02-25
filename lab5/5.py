import re

def match_strings(filename):
    with open(filename, 'r',encoding='utf-8') as file:
        text = file.read()
    
    pattern = r'a.*b\b'
    matches = re.findall(pattern, text)
    
    return matches

filename = 'lab5/row.txt' 
matching_strings = match_strings(filename)
print("Strings matching the pattern:")
for string in matching_strings:
    print(string)