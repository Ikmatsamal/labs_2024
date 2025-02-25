import re

with open('lab5/camel.txt', 'r', encoding='utf-8') as file:
    text = file.read()
    result = re.sub(r'(?<!^)(?=[A-Z])', '_',  text).strip()

    print(result)
