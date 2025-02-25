import re
def match_pattern(string):
    pattern = r'ab{2,3}'
    if re.fullmatch(pattern, string):
        return True
    else:
        return False

strings = ['abb', 'abbb', 'a', 'ab', 'abc', 'abbbb', 'abbbbbc']
for s in strings:
    print(f"{s}: {match_pattern(s)}")