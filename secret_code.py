# Imports
import math

# Defining functions
def matrix(side, string):
    out = []
    list_string = list(string)
    for i in range(0, side):
        straight = []
        if i == 0:
            straight.append(list_string[0: ((i+1)*side)])
        else:
            straight.append(list_string[((i*side) ): ((i+1)*side)])
        out.extend(straight)
    return out

# All inputs
n = int(input())
# Begin Solution
for i in range(0,n):
    code = input()
    length = len(code)
    side = int(math.sqrt(length))
    encrypt = matrix(side, code)
    decrypt = []
    for column in range(0, side):
        ex = []
        for row in range(0, side):
            ex.extend(encrypt[row][column])
        decrypt.append(''.join(ex))
    result = decrypt[::-1]
    print(''.join(result))
