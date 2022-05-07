input = input()
list = input.split(";")
count = 0

for i in list:
    if ("-" in i):
        new_list = i.split("-")
        n = int(new_list[1]) - int(new_list[0]) + 1
        count += n
    else:
        count += 1

print(count)
        