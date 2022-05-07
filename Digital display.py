def N1():
    if line in [1, 4, 7]:
        return [4*' ', '+']
    else:
        return [4*' ', '|']


def N2():
    if line in [1, 4, 7]:
        return ['+', 3*'-', '+']
    elif line in [2, 3]:
        return [4*' ', '|']
    else:
        return ['|', 4*' ']


def N3():
    if line in [1, 4, 7]:
        return ['+', 3*'-', '+']
    else:
        return [4*' ', '|']


def N4():
    if line == 1:
        return ['+', 3*' ', '+']
    elif line in [2, 3]:
        return ['|', 3*' ', '|']
    elif line == 4:
        return ['+', 3*'-', '+']
    elif line in [5, 6]:
        return [4*' ', '|']
    else:
        return [4*' ', '+']


def N5():
    if line in [1, 4, 7]:
        return ['+', 3*'-', '+']
    elif line in [5, 6]:
        return [4*' ', '|']
    else:
        return ['|', 4*' ']


def N6():
    if line in [1, 4, 7]:
        return ['+', 3*'-', '+']
    elif line in [5, 6]:
        return ['|', 3*' ', '|']
    else:
        return ['|', 4*' ']


def N7():
    if line == 1:
        return ['+', 3*'-', '+']
    elif line in [4, 7]:
        return [4*' ', '+']
    else:
        return [4*' ', '|']


def N8():
    if line in [1, 4, 7]:
        return ['+', 3*'-', '+']
    else:
        return ['|', 3*' ', '|']


def N9():
    if line in [1, 4, 7]:
        return ['+', 3*'-', '+']
    elif line in [5, 6]:
        return [4*' ', '|']
    else:
        return ['|', 3*' ', '|']


def N0():
    if line in [1, 7]:
        return ['+', 3*'-', '+']
    elif line == 4:
        return ['+', 3*' ', '+']
    else:
        return ['|', 3*' ', '|']    


def N():
    if line in [1, 2, 4, 6, 7]:
        return [' ']
    else:
        return ['o']


numbers = {'1': N1,
           '2': N2,
           '3': N3,
           '4': N4,
           '5': N5,
           '6': N6,
           '7': N7,
           '8': N8,
           '9': N9,
           '0': N0,
           ':': N}


while True:
    time = input()
    if time == 'end':
        print(time)
        break
    else:
        time = list(time)
        line = 1
        while line < 8:
            printed = []
            for x in time:
                func = numbers[x]
                printed.append(''.join(func()))
            print('  '.join(printed))
            line = line + 1
        print('')
        print('')