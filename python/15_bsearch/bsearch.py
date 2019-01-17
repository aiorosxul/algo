list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
value = 1
flag = 0


def Bsearch(list, value, flag) -> int:
    try:
        mid = len(list) // 2
        flag += mid
        if value == list[mid]:
            return flag
        elif value < list[mid]:
            return Bsearch(list[:mid], value, flag)
        else:
            return Bsearch(list[mid:], value, flag)
    except IndexError:
        print('Value not found!')


print(Bsearch(list, value, flag))
