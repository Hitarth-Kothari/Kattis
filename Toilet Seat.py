def policy_1(line):
    count = 0
    for i in range(1, len(line)):
        if i == 1:
            if line[i] == 'D':
                if line[0] == 'D':
                    count = count + 1
                else:
                    count = count + 2
            else:
                if line[0] != 'U':
                    count = count + 1 
        elif line[i] == 'D':
            count = count + 2 

    return count


def policy_2(line):
    count = 0
    for i in range(1, len(line)):
        if i == 1:
            if line[i] == 'U':
                if line[0] == 'U':
                    count = count + 1
                else:
                    count = count + 2
            else:
                if line[0] != 'D':
                    count = count + 1
        elif line[i] == 'U':
            count = count + 2 
    return count


def policy_3(line):
    count = 0
    for i in range(1, len(line)):
        if line[i] != line [i - 1]:
            count = count + 1
    return count


x = input()
line = list(x)
print(policy_1(line))
print(policy_2(line))
print(policy_3(line))