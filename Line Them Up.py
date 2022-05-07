n = int(input())
f = []
assending = False
desending = False
check = [desending, assending]
for i in range(0, n):
    l = list(input())
    f.append(l)
for i in range(0, n-1):
    if f[i] > f[i + 1]:
        check[0] = True
    elif f[i] < f[i + 1]:
        check[1] = True

if check == [True, False]:
    print('DECREASING')
elif check == [False, True]:
    print('INCREASING')
else:
    print('NEITHER')