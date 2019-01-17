def merge_sort(list):
    if len(list) == 1:
        return list
    else:
        mid = len(list) // 2
        left = list[:mid]
        right = list[mid:]
        l1 = merge_sort(left)
        r1 = merge_sort(right)
        return merge(l1, r1)


def merge(left, right):
    result = []
    while len(left) > 0 and len(right) > 0:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    result += left
    result += right
    return result


print(merge_sort(list))
