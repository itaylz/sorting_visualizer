import visualizer


def insertion_sort(draw_info, ascending=True):
    lst = draw_info.lst

    for i in range(1, len(lst)):
        current = lst[i]

        while True:
            ascending_sort = i > 0 and lst[i - 1] > current and ascending
            descending_sort = i > 0 and lst[i - 1] < current and not ascending

            if not ascending_sort and not descending_sort:
                break

            lst[i] = lst[i - 1]
            i = i - 1
            lst[i] = current
            visualizer.draw_list(draw_info, {i - 1: draw_info.RED, i: draw_info.ORANGE, i + 1: draw_info.YELLOW, i + 2: draw_info.GREEN, i + 3: draw_info.BLUE, i + 4: draw_info.PURPLE}, True)
            yield True

    return lst