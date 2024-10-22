import visualizer


def shaker_sort(draw_info, ascending=True):
    lst = draw_info.lst
    n = len(lst)
    left = 0
    right = n - 1

    if ascending:
        while True:
            for i in range(left, right):
                if lst[i] > lst[i + 1]:
                    temp = lst[i]
                    lst[i] = lst[i + 1]
                    lst[i + 1] = temp
                    visualizer.draw_list(draw_info, {i - 1: draw_info.RED, i: draw_info.ORANGE, i + 1: draw_info.YELLOW, i + 2: draw_info.GREEN, i + 3: draw_info.BLUE, i + 4: draw_info.PURPLE},True)

            right -= 1

            for i in range(right, left, -1):
                if lst[i] < lst[i - 1]:
                    temp = lst[i]
                    lst[i] = lst[i - 1]
                    lst[i - 1] = temp
                    visualizer.draw_list(draw_info, {i - 1: draw_info.RED, i: draw_info.ORANGE, i + 1: draw_info.YELLOW, i + 2: draw_info.GREEN, i + 3: draw_info.BLUE, i + 4: draw_info.PURPLE}, True)

            left += 1
            yield True

            if left >= right:
                break
    else:
        while True:
            for i in range(left, right):
                if lst[i] < lst[i + 1]:
                    temp = lst[i]
                    lst[i] = lst[i + 1]
                    lst[i + 1] = temp
                    visualizer.draw_list(draw_info, {i - 1: draw_info.RED, i: draw_info.ORANGE, i + 1: draw_info.YELLOW, i + 2: draw_info.GREEN, i + 3: draw_info.BLUE, i + 4: draw_info.PURPLE}, True)

            right -= 1

            for i in range(right, left, -1):
                if lst[i] > lst[i - 1]:
                    temp = lst[i]
                    lst[i] = lst[i - 1]
                    lst[i - 1] = temp
                    visualizer.draw_list(draw_info, {i - 1: draw_info.RED, i: draw_info.ORANGE, i + 1: draw_info.YELLOW, i + 2: draw_info.GREEN, i + 3: draw_info.BLUE, i + 4: draw_info.PURPLE}, True)

            left += 1
            yield True

            if left >= right:
                break
