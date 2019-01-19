"""
    Author: aiorosxu
"""


# 有重复数组，返回第一个查找到的元素位置
def Bsearch_first(list, value) -> int:
    start = 0
    end = len(list)
    while start <= end:
        mid = start + (end - start) // 2
        if list[mid] > value:
            end = mid - 1
        elif list[mid] < value:
            start = mid + 1
        else:
            if (mid == 0) or (list[mid - 1] != value):
                return mid
            else:
                end = mid - 1

    return -1


# 有重复数组，返回最后一个查找到的元素的位置
def Bsearch_last(list, value) -> int:
    start = 0
    end = len(list)
    while start <= end:
        mid = start + (end - start) // 2
        if list[mid] > value:
            end = mid - 1
        elif list[mid] < value:
            start = mid + 1
        else:
            if (mid == 0) or (list[mid + 1] != value):
                return mid
            else:
                start = mid + 1

    return -1


# 有重复数组，返回第一个大于等于所查找元素的位置
def Bsearch_first_greater(list, value) -> int:
    start = 0
    end = len(list)
    while start <= end:
        mid = start + (end - start) // 2
        if list[mid] > value:
            if mid == 0 or list[mid - 1] < value:
                return mid
            else:
                end = mid - 1
        else:
            start = mid + 1

    return -1


# 有重复数组，返回最后一个小于等于所查找元素的位置
def Bsearch_last_less(list, value) -> int:
    start = 0
    end = len(list)
    while start <= end:
        mid = start + (end - start) // 2
        if list[mid] < value:
            if mid == 0 or list[mid + 1] > value:
                return mid
            else:
                start = mid + 1
        else:
            end = mid - 1

    return -1


list = [0, 1, 2, 2, 3, 3, 6, 7, 8, 9]
value = 5
print(Bsearch_last_less(list, value))
