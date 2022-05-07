while True:
    x, y = map(int, input().split())
    print(abs(x - y))

    if x is None:
        break