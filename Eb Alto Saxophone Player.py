cords = {'c': [2,3,4,7,8,9,10],
         'd': [2,3,4,7,8,9], 
         'e': [2,3,4,7,8],
         'f': [2,3,4,7],
         'g': [2,3,4],
         'a': [2,3],
         'b': [2],
         'C': [3],
         'D': [1,2,3,4,7,8,9],
         'E': [1,2,3,4,7,8],
         'F': [1,2,3,4,7],
         'G': [1,2,3,4],
         'A': [1,2,3],
         'B': [1,2] }

n = int(input())

for i in range(0, n):
    fingers = {1: 0,
           2: 0,
           3: 0,
           4: 0,
           5: 0,
           6: 0,
           7: 0,
           8: 0,
           9: 0,
           10: 0}
    current = []
    result = []
    cord = list(input())
    for x in cord:
        for y in cords[x]:
            if y not in current:
                fingers[y] = fingers[y] + 1
        current = cords[x]
    for x in fingers:
        result.append(str(fingers[x]))
    print(' '.join(result))

