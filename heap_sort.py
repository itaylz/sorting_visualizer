import visualizer
import heapq

def heap_sort(draw_info, ascending=True):
    lst = draw_info.lst
    heapq.heapify(lst)
    n = len(lst)
    new_lst = [0]*n
    for i in range(n):
        new_lst[i] = lst[i]
    if ascending:
        for i in range(n):
            min_ = heapq.heappop(new_lst)
            lst[i] = min_
            visualizer.draw_list(draw_info, {min_: draw_info.RED, i: draw_info.ORANGE, i + 1: draw_info.YELLOW, i + 2: draw_info.GREEN, i + 3: draw_info.BLUE, i + 4: draw_info.PURPLE}, True)
            yield True
    else:
        for i in reversed(range(n)):
            min_ = heapq.heappop(new_lst)
            lst[i] = min_
            visualizer.draw_list(draw_info, {min_: draw_info.RED, i: draw_info.ORANGE, i + 1: draw_info.YELLOW, i + 2: draw_info.GREEN, i + 3: draw_info.BLUE, i + 4: draw_info.PURPLE}, True)
            yield True

    return new_lst
