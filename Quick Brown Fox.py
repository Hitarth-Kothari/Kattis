import string


n = int(input())
for i in range(0, n):
    there = []
    line = set(list(input().lower()))
    count = 0
    for x in line:
        if x in string.ascii_lowercase:
            count = count + 1
            there.append(x)

    if count == 26:
        print('pangram')
    else:
        missing = sorted(list(set(string.ascii_lowercase) - set(there)))
        print('missing {}'.format(''.join(missing)))