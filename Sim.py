n = int(input())
for i in range(0, n):
    line = list(input())
    x = 0
    y = 0
    while True:
        if x < len(line):
            if line[x] == '<':
                pos = x
                if pos == 0:
                    del line[pos]
                    x = -1
                else:
                    del line[pos]
                    i = 1
                    while True:
                        if line[pos - i] in ['[', ']']:
                            i = i + 1
                        else:
                            del line[pos - i]
                            break
                    x = pos - 2
            x = x + 1
        else:
            break

    while True:
        
        if '[' in line:
            if ']' in line:
                pos1 = line.index('[')
                pos2 = line.index(']')
                home = line[pos1 + 1 : pos2]
                del line[pos1: pos2 + 1]
                line = home + line
            else:
                for i in range(0, line.count('[')):
                    line.remove('[')
        else:
            for i in range(0, line.count(']')):
                line.remove(']')
            break
    print(''.join(line))