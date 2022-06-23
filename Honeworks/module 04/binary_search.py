def BinarySearch(lst, val):
    first = 0
    last = len(lst) - 1
    index = -1
    while (first <= last) and (index == -1):
        mid = (first + last) // 2
        if lst[mid] == val:
            index = mid
        else:
            if val < lst[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return index
    