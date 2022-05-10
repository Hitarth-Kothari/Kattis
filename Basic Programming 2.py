# Take first line of inputs and convert to int
N_and_t = input().split(" ")
N = int(N_and_t[0])
t = int(N_and_t[1])
# Take array of string and convert to array of int
array = input().split(" ")
for i in range(0, N):
    array[i] = int(array[i])
# Run tasks based on t
tool = False
if t == 1:
    for i in range(0, N):
        for j in range(i + 1, N):
            if array[i] != array[j]:
                if (array[i] + array[j] == 7777):
                    print("Yes")
                    tool = True
                    break
    if tool == False:
        print("No")
elif t == 2:
    for i in range(0, N):
        for j in range(i + 1, N):
            if array[i] == array[j]:
                print("Contains duplicate")
                tool = True
                break
    if tool == False:
        print("Unique")
elif t == 3:
    for i in array:
        if array.count(i) >= N/2:
            print(i)
            tool = True
            break
    if tool == False:
        print("-1")
elif t == 4:
    if N%2 == 0:
        array.sort()
        print("{} {}".format(array[int((N/2)-1)], array[int(N/2)]))
    else:
        array.sort()
        print(array(int((N+1)/2)))
elif t == 5:
    array.sort()
    for i in array:
        if i in range(100, 1000):
            print(i, end = " ")