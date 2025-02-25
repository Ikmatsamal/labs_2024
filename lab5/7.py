import re

def snake_to_camel(s):
    return re.sub(r'_([a-z])', lambda match: match.group(1).upper(), s)

with open('lab5/snake.txt', 'r', encoding='utf-8') as file:
    text = file.read().strip()

camel_case = snake_to_camel(text)

print(camel_case)
