import re

with open('lab5/row.txt', 'r', encoding='utf-8') as file:
    text = file.read().strip()

result = re.split(r'(?=[A-ZА-Я])', text)

print(result)
