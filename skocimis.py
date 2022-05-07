x, y, z = map(int, input().split())
if y - x > z - y:
    print(y-x-1)
else:
    print(z-y-1)2