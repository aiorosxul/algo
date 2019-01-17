def quick_sort(list):
    if len(list) == 1:
        return list
    flag = list[len(list) // 2]
    mid = [x for x in list if x == flag]
    left = [x for x in list if x < flag]
    right = [x for x in list if x > flag]
    return quick_sort(left) + mid + quick_sort(right)
