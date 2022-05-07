loop = True
while loop == True:
    calls, intervals = map(int, input().split())
    if calls ==  intervals == 0:
        loop = False
        break
    call_list = []
    for i in range(0, calls):
        call_list.append(list(map(int, input().split())))
    for i in range(0, intervals):
        count = 0
        x, y = map(int, input().split())
        for j in range(0, calls):
            if x >= call_list[j][2] and x < sum(call_list[j][2:4]):
                count = count + 1
            elif x + y > call_list[j][2] and x + y <= sum(call_list[j][2:4]):
                count = count + 1
            elif x < call_list[j][2] and x + y > sum(call_list[j][2:4]):
                count = count + 1
        print(count)
