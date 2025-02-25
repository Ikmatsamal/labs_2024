import re
def match_pattern(string):
    pattern = r'ab*'
    if re.fullmatch(pattern, string):
        return True
    else:
        return False
strings = ['a', 'ab', 'abb', 'abbb', 'ac', 'abc', 'abbc']
for s in strings:
    print(f"{s}: {match_pattern(s)}")