def insert_sort(list):
    for i in range(1, len(list)):
        for j in range(i, 0, -1):
            if list[j] < list[j - 1]:
                list[j - 1], list[j] = list[j], list[j - 1]
    return list

def bubble_sort(list):
    for n in range(len(list)):
        for i in range(len(list) - 1, 0, -1):
            if list[i] > list[i - 1]:
                list[i - 1], list[i] = list[i], list[i - 1]
    return list

def select_sort(list):
    for j in range(len(list) - 1):
        for i in range(len(list) - 1, j, -1):
            if list[i] < list[i - 1]:
                list[i - 1], list[i] = list[i], list[i - 1]
    return list
