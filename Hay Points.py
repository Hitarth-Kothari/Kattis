n, m = map(int, input().split())
hay = {}
for i in range(0, n):
    x, y = map(str, input().split())
    y = int(y)
    hay[x] = y
for i in range(0, m):
    score = 0
    while True:
        cv = input().split()
        if cv == ['.']:
            break
        else:
            for x in cv:
                if x in hay:
                    score = score + hay[x]
    print(score)
        