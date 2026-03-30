def quick_sort(int_list):
    if len(int_list) <= 1:
        return int_list

    pivot = int_list[-1]

    less = [x for x in int_list if x < pivot]
    equal = [x for x in int_list if x == pivot]
    greater = [x for x in int_list if x > pivot]

    return quick_sort(less) + equal + quick_sort(greater)
