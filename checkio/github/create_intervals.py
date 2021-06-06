data = {1, 2, 3, 6, 7, 8, 4, 5}
data_list = sorted(list(data))

result = []

start = data_list[0]
for i in range(1, len(data_list)):
    if data_list[i] - data_list[i-1] == 1:
        continue
    else:
        result.append((start, data_list[i-1]))
        start = data_list[i]
        if i == len(data_list) - 1:
            result.append((start, start))
        # result.append((start, data_list[i]))

print(result)