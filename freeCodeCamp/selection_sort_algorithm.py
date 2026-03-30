def selection_sort(list_in):
    length = len(list_in)

    for i in range(length - 1):
        min_index = i

        for j in range(i + 1, length):
            if list_in[j] < list_in[min_index]:
                min_index = j

        if min_index != i:
            list_in[i], list_in[min_index] = list_in[min_index], list_in[i]

    return list_in
