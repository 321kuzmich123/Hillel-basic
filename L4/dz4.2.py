lst = [0, 1, 7, 2, 4, 8]

if not lst:
    print([])
else:
    sum_index = 0
    for i in range(0, len(lst), 2):
        sum_index += lst[i]
    result =sum_index * lst[-1]
    print(result)