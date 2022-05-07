input = input()
list = input.split(";")
count = 0

for i in list:
    if len(i)>=3 and ("-" in i):
        new_list = i.split("-")
        n = int(new_list[1]) - int(new_list[0]) + 1
        count += n
    else:
        count += 1

print(count)
        