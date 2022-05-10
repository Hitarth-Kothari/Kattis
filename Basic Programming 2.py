from collections import Counter

if __name__ == "__main__":
    # Take first line of inputs and convert to int
    N_and_t = input().split(" ")
    N = int(N_and_t[0])
    t = int(N_and_t[1])
    # Take array of string and convert to array of int
    array = input().split(" ")
    for i in range(0, N):
        array[i] = int(array[i])
    # Run tasks based on t
    if t == 1:
        s = set(array)
        for i in range(1, 7777):
            if i in s and (7777 - i) in s:
                print("Yes")
                break
        else:
            print("No")
    elif t == 2:
        if len(set(array)) == N:
            print("Unique")
        else:
            print("Contains duplicate")
    elif t == 3:
        a,b = Counter(array).most_common(1)[0]
        if b > N/2:
            print(a)
        else:
            print(-1,)
    elif t == 4:
        if N%2 == 0:
            array.sort()
            print("{} {}".format(array[int((N/2)-1)], array[int(N/2)]))
        else:
            array.sort()
            n = array[int((N-1)/2)]
            print(n)
    elif t == 5:
        array.sort()
        for i in (array):
            if i in range(100, 1000):
                print(i, end = " ")