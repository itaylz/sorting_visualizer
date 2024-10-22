import visualizer


def merge_sort(draw_info, ascending=True):
    # start with least partition size of 2^0 = 1
    lst = draw_info.lst
    width = 1
    n = len(lst)
    # subarray size grows by powers of 2
    # since growth of loop condition is exponential,
    # time consumed is logarithmic (log2n)
    while (width < n):
        # always start from leftmost
        l = 0;
        while (l < n):
            r = min(l + (width * 2 - 1), n - 1)
            m = min(l + width - 1, n - 1)
            # final merge should consider
            # unmerged sublist if input arr
            # size is not power of 2
            merge(lst, l, m, r,draw_info, ascending)
            l += width * 2
        # Increasing sub array size by powers of 2
        width *= 2
    yield True
    return lst


# Merge Function
def merge(lst, l, m, r,draw_info, ascending):
    n1 = m - l + 1
    n2 = r - m
    L = [0] * n1
    R = [0] * n2
    for i in range(0, n1):
        L[i] = lst[l + i]
    for i in range(0, n2):
        R[i] = lst[m + i + 1]

    i, j, k = 0, 0, l
    if ascending:
        while i < n1 and j < n2:
            if L[i] <= R[j]:
                lst[k] = L[i]
                i += 1
            else:
                lst[k] = R[j]
                j += 1
            k += 1
            visualizer.draw_list(draw_info, {i: draw_info.RED, i + 1: draw_info.ORANGE, j: draw_info.YELLOW, j + 1: draw_info.GREEN, k: draw_info.BLUE, k + 1: draw_info.PURPLE}, True)


    else:
        while i < n1 and j < n2:
            if L[i] >= R[j]:
                lst[k] = L[i]
                i += 1
            else:
                lst[k] = R[j]
                j += 1
            k += 1
            visualizer.draw_list(draw_info, {i: draw_info.RED, i + 1: draw_info.ORANGE, j: draw_info.YELLOW, j + 1: draw_info.GREEN, k: draw_info.BLUE, k + 1: draw_info.PURPLE}, True)


    while i < n1:
        lst[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        lst[k] = R[j]
        j += 1
        k += 1



