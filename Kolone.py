N1, N2 = map(int, input().split())
line1 = list(input())
line1 = line1[::-1]
line2 = list(input())
time = int(input())
for i in range (time, 0, -1):
    if line2 != []:
        N = len(line1)
        if i <= N:
            line1.insert(N - i, line2[0])
            del line2[0]
        else:
            if (i - N) <= len(line2) - 1:
                line1.insert(0, line2[i - N])
                del line2[i - N]
            else:
                line1.insert(0, line2[-1])
                del line2[-1]
    if line2 == []:
        break

line = line1 + line2
print(''.join(line))
