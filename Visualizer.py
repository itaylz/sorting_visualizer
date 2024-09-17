import pygame
import random
import math
import heapq


pygame.init()


class DrawInformation:
    BLACK = 0, 0, 0
    WHITE = 255, 255, 255
    GREEN = 0, 255, 0
    RED = 255, 0, 0
    BLUE = 0, 0, 255
    YELLOW = 255, 255, 0
    PURPLE = 153, 51, 255
    ORANGE = 255, 153, 0

    BACKGROUND_COLOR = WHITE

    GRADIENTS = [
        (128, 128, 128),
        (160, 160, 160),
        (192, 192, 192)
    ]

    FONT = pygame.font.SysFont('Arial', 25)
    LARGE_FONT = pygame.font.SysFont('Arial', 40)

    SIDE_PAD = 200
    TOP_PAD = 300

    def __init__(self, width, height, lst):
        self.width = width
        self.height = height

        self.window = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Sorting Algorithm Visualization")
        self.set_list(lst)

    def set_list(self, lst):
        self.lst = lst
        self.min_val = min(lst)
        self.max_val = max(lst)

        self.block_width = round((self.width - self.SIDE_PAD) / len(lst))
        self.block_height = math.floor((self.height - self.TOP_PAD) / (self.max_val - self.min_val))
        self.start_x = self.SIDE_PAD // 2


def draw(draw_info, algo_name, ascending):
    draw_info.window.fill(draw_info.BACKGROUND_COLOR)

    title = draw_info.LARGE_FONT.render(f"{algo_name} - {'Ascending' if ascending else 'Descending'}", 1,
                                        draw_info.BLUE)
    draw_info.window.blit(title, (draw_info.width / 2 - title.get_width() / 2, 5))

    controls = draw_info.FONT.render("R - Reset | SPACE - Start Sorting | A - Ascending | D - Descending", 1,
                                     draw_info.BLACK)
    draw_info.window.blit(controls, (draw_info.width / 2 - controls.get_width() / 2, 60))

    sorting = draw_info.FONT.render("I - Insertion Sort | B - Bubble Sort | M - Merge Sort | Q - Quick Sort"
                                    , 1, draw_info.BLACK)
    draw_info.window.blit(sorting, (draw_info.width / 2 - sorting.get_width() / 2, 90))

    sorting_2 = draw_info.FONT.render("H - Heap Sort | C - Shaker Sort | S - Selection Sort", 1, draw_info.BLACK)

    draw_info.window.blit(sorting_2, (draw_info.width / 2 - sorting_2.get_width() / 2, 120))

    draw_list(draw_info)
    pygame.display.update()


def draw_list(draw_info, color_positions={}, clear_bg=False):
    lst = draw_info.lst

    if clear_bg:
        clear_rect = (draw_info.SIDE_PAD // 2, draw_info.TOP_PAD,
                      draw_info.width - draw_info.SIDE_PAD, draw_info.height - draw_info.TOP_PAD)
        pygame.draw.rect(draw_info.window, draw_info.BACKGROUND_COLOR, clear_rect)

    for i, val in enumerate(lst):
        x = draw_info.start_x + i * draw_info.block_width
        y = draw_info.height - (val - draw_info.min_val) * draw_info.block_height

        color = draw_info.GRADIENTS[i % 3]

        if i in color_positions:
            color = color_positions[i]

        pygame.draw.rect(draw_info.window, color, (x, y, draw_info.block_width, draw_info.height))

    if clear_bg:
        pygame.display.update()


def generate_starting_list(n, min_val, max_val):
    lst = []

    for _ in range(n):
        val = random.randint(min_val, max_val)
        lst.append(val)

    return lst

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
            draw_list(draw_info, {i: draw_info.RED, i + 1: draw_info.ORANGE, j: draw_info.YELLOW, j + 1: draw_info.GREEN, k: draw_info.BLUE, k + 1: draw_info.PURPLE}, True)


    else:
        while i < n1 and j < n2:
            if L[i] >= R[j]:
                lst[k] = L[i]
                i += 1
            else:
                lst[k] = R[j]
                j += 1
            k += 1
            draw_list(draw_info, {i: draw_info.RED, i + 1: draw_info.ORANGE, j: draw_info.YELLOW, j + 1: draw_info.GREEN, k: draw_info.BLUE, k + 1: draw_info.PURPLE}, True)


    while i < n1:
        lst[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        lst[k] = R[j]
        j += 1
        k += 1



def quick_sort(draw_info, ascending=True):
    lst = draw_info.lst
    quick_sort2(lst,0,len(lst) - 1,draw_info, ascending)
    yield True
    return lst


def quick_sort2(lst, left, right,draw_info, ascending=True):
    draw_list(draw_info, {left: draw_info.RED, left + 1: draw_info.ORANGE, left + 2: draw_info.YELLOW, right - 1: draw_info.GREEN, right: draw_info.BLUE}, True)

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
                draw_list(draw_info, {l: draw_info.RED, l + 1: draw_info.ORANGE, l + 2: draw_info.YELLOW, r - 1: draw_info.GREEN, r: draw_info.BLUE, pivot: draw_info.PURPLE}, True)


        if lst[l] > pivot:
            lst[l], lst[right] = lst[right], lst[l]
            draw_list(draw_info, {l: draw_info.RED, l + 1: draw_info.ORANGE, l + 2: draw_info.YELLOW, r - 1: draw_info.GREEN, r: draw_info.BLUE, pivot: draw_info.PURPLE}, True)

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
                draw_list(draw_info, {l: draw_info.RED, l + 1: draw_info.ORANGE, l + 2: draw_info.YELLOW, r - 1: draw_info.GREEN, r: draw_info.BLUE, pivot: draw_info.PURPLE}, True)

        if lst[l] < pivot:
            lst[l], lst[right] = lst[right], lst[l]
            draw_list(draw_info, {l: draw_info.RED, l + 1: draw_info.ORANGE, l + 2: draw_info.YELLOW, r - 1: draw_info.GREEN, r: draw_info.BLUE, pivot: draw_info.PURPLE}, True)

        return l


def bubble_sort(draw_info, ascending=True):
    lst = draw_info.lst
    for i in range(len(lst) - 1):
        for j in range(len(lst) - 1 - i):
            num1 = lst[j]
            num2 = lst[j + 1]

            if (num1 > num2 and ascending) or (num1 < num2 and not ascending):
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                draw_list(draw_info, {j: draw_info.RED, j + 1: draw_info.ORANGE, j + 2: draw_info.YELLOW, j + 3: draw_info.GREEN, j + 4: draw_info.BLUE, j + 5: draw_info.PURPLE}, True)
                yield True

    return lst


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
            draw_list(draw_info, {i - 1: draw_info.RED, i: draw_info.ORANGE, i + 1: draw_info.YELLOW, i + 2: draw_info.GREEN, i + 3: draw_info.BLUE, i + 4: draw_info.PURPLE}, True)
            yield True

    return lst


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
            draw_list(draw_info, {min_: draw_info.RED, i: draw_info.ORANGE, i + 1: draw_info.YELLOW, i + 2: draw_info.GREEN, i + 3: draw_info.BLUE, i + 4: draw_info.PURPLE}, True)
            yield True
    else:
        for i in reversed(range(n)):
            min_ = heapq.heappop(new_lst)
            lst[i] = min_
            draw_list(draw_info, {min_: draw_info.RED, i: draw_info.ORANGE, i + 1: draw_info.YELLOW, i + 2: draw_info.GREEN, i + 3: draw_info.BLUE, i + 4: draw_info.PURPLE}, True)
            yield True

    return new_lst


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
                    draw_list(draw_info, {i - 1: draw_info.RED, i: draw_info.ORANGE, i + 1: draw_info.YELLOW, i + 2: draw_info.GREEN, i + 3: draw_info.BLUE, i + 4: draw_info.PURPLE},True)

            right -= 1

            for i in range(right, left, -1):
                if lst[i] < lst[i - 1]:
                    temp = lst[i]
                    lst[i] = lst[i - 1]
                    lst[i - 1] = temp
                    draw_list(draw_info, {i - 1: draw_info.RED, i: draw_info.ORANGE, i + 1: draw_info.YELLOW, i + 2: draw_info.GREEN, i + 3: draw_info.BLUE, i + 4: draw_info.PURPLE}, True)

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
                    draw_list(draw_info, {i - 1: draw_info.RED, i: draw_info.ORANGE, i + 1: draw_info.YELLOW, i + 2: draw_info.GREEN, i + 3: draw_info.BLUE, i + 4: draw_info.PURPLE}, True)

            right -= 1

            for i in range(right, left, -1):
                if lst[i] > lst[i - 1]:
                    temp = lst[i]
                    lst[i] = lst[i - 1]
                    lst[i - 1] = temp
                    draw_list(draw_info, {i - 1: draw_info.RED, i: draw_info.ORANGE, i + 1: draw_info.YELLOW, i + 2: draw_info.GREEN, i + 3: draw_info.BLUE, i + 4: draw_info.PURPLE}, True)

            left += 1
            yield True

            if left >= right:
                break


def selection_sort(draw_info, ascending=True):
	lst = draw_info.lst

	for i in range(0, len(lst)-1):
		min = i

		for j in range(i+1, len(lst)):
			if (lst[j] < lst[min] and ascending) or (lst[j] > lst[min] and not ascending):
				min = j

		if min != i:
			lst[min], lst[i] = lst[i], lst[min]
			draw_list(draw_info, {min: draw_info.RED, i: draw_info.ORANGE, i + 1: draw_info.YELLOW, i + 2: draw_info.GREEN, i + 3: draw_info.BLUE, i + 4: draw_info.PURPLE},  True)
			yield True

	return lst


def main():
    run = True
    clock = pygame.time.Clock()

    n = 100
    min_val = 0
    max_val = 100

    lst = generate_starting_list(n, min_val, max_val)
    draw_info = DrawInformation(1000, 700, lst)
    sorting = False
    ascending = True

    sorting_algorithm = merge_sort
    sorting_algo_name = "Merge Sort"
    sorting_algorithm_generator = None

    while run:
        clock.tick(60)

        if sorting:
            try:
                next(sorting_algorithm_generator)
            except StopIteration:
                sorting = False
        else:
            draw(draw_info, sorting_algo_name, ascending)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type != pygame.KEYDOWN:
                continue

            if event.key == pygame.K_r:
                lst = generate_starting_list(n, min_val, max_val)
                draw_info.set_list(lst)
                sorting = False
            elif event.key == pygame.K_SPACE and sorting == False:
                sorting = True
                sorting_algorithm_generator = sorting_algorithm(draw_info, ascending)
            elif event.key == pygame.K_a and not sorting:
                ascending = True
            elif event.key == pygame.K_d and not sorting:
                ascending = False
            elif event.key == pygame.K_i and not sorting:
                sorting_algorithm = insertion_sort
                sorting_algo_name = "Insertion Sort"
            elif event.key == pygame.K_b and not sorting:
                sorting_algorithm = bubble_sort
                sorting_algo_name = "Bubble Sort"
            elif event.key == pygame.K_m and not sorting:
                sorting_algorithm = merge_sort
                sorting_algo_name = "Merge Sort"
            elif event.key == pygame.K_q and not sorting:
                sorting_algorithm = quick_sort
                sorting_algo_name = "Quick Sort"
            elif event.key == pygame.K_h and not sorting:
                sorting_algorithm = heap_sort
                sorting_algo_name = "Heap Sort"
            elif event.key == pygame.K_c and not sorting:
                sorting_algorithm = shaker_sort
                sorting_algo_name = "Shaker Sort"
            elif event.key == pygame.K_s and not sorting:
                sorting_algorithm = selection_sort
                sorting_algo_name = "Selection Sort"


    pygame.quit()


if __name__ == "__main__":
    main()