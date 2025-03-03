def determine( test):
    rev = (test == ''.join(list(reversed(test))))
    nn="not "
    if rev:
        nn=""
    print(f'Test {test} is {nn}palindrom')


a = input()

determine(a)
