import visualizer


def quick_sort(draw_info, ascending=True):
    lst = draw_info.lst
    quick_sort2(lst,0,len(lst) - 1,draw_info, ascending)
    yield True
    return lst


def quick_sort2(lst, left, right,draw_info, ascending=True):
    visualizer.draw_list(draw_info, {left: draw_info.RED, left + 1: draw_info.ORANGE, left + 2: draw_info.YELLOW, right - 1: draw_info.GREEN, right: draw_info.BLUE}, True)

    if left < right:
        # recursive calls on partitions of array from start to middle and from middle to len
        partition_pos = partition(lst, left, right,draw_info, ascending)
        quick_sort2(lst, left, partition_pos - 1,draw_info, ascending)
        quick_sort2(lst, partition_pos + 1, right,draw_info, ascending)

#does the actual sorting of lists by swapping positions of elements
def partition(lst, left, right, draw_info, ascending):
    if ascending:
        l = left
        r = right - 1
        pivot = lst[right]

        while l < r:
            while l < right and lst[l] < pivot:
                l += 1

            while r > left and lst[r] >= pivot:
                r -= 1

            if l < r:
                lst[l], lst[r] = lst[r], lst[l]
                visualizer.draw_list(draw_info, {l: draw_info.RED, l + 1: draw_info.ORANGE, l + 2: draw_info.YELLOW, r - 1: draw_info.GREEN, r: draw_info.BLUE, pivot: draw_info.PURPLE}, True)


        if lst[l] > pivot:
            lst[l], lst[right] = lst[right], lst[l]
            visualizer.draw_list(draw_info, {l: draw_info.RED, l + 1: draw_info.ORANGE, l + 2: draw_info.YELLOW, r - 1: draw_info.GREEN, r: draw_info.BLUE, pivot: draw_info.PURPLE}, True)

        return l
    else:
        l = left
        r = right - 1
        pivot = lst[right]

        while l < r:
            while l < right and lst[l] > pivot:
                l += 1

            while r > left and lst[r] <= pivot:
                r -= 1

            if l < r:
                lst[l], lst[r] = lst[r], lst[l]
                visualizer.draw_list(draw_info, {l: draw_info.RED, l + 1: draw_info.ORANGE, l + 2: draw_info.YELLOW, r - 1: draw_info.GREEN, r: draw_info.BLUE, pivot: draw_info.PURPLE}, True)

        if lst[l] < pivot:
            lst[l], lst[right] = lst[right], lst[l]
            visualizer.draw_list(draw_info, {l: draw_info.RED, l + 1: draw_info.ORANGE, l + 2: draw_info.YELLOW, r - 1: draw_info.GREEN, r: draw_info.BLUE, pivot: draw_info.PURPLE}, True)

        return l

