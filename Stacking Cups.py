import string

n = int(input())
stack = {}
for i in range(0, n):
    x, y = map(str, input().split())
    if x.isdigit():
        stack[int(x)/2] = y
    else:
        stack[int(y)] = x
keys = sorted(stack)
for x in keys:
    print(stack[x])
