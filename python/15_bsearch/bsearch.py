list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
value = 7


def Bsearch(list, value, start=0, end=None) -> int:
    end = len(list) if end is None else end
    mid = start + (end - start) // 2
    if start <= end:
        if value == list[mid]:
            return mid
        elif value < list[mid]:
            return Bsearch(list, value, start=start, end=mid - 1)
        else:
            return Bsearch(list, value, start=mid + 1, end=end)
    else:
        print('Not found')

print(Bsearch(list, value))
