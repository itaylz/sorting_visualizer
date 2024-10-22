import pygame
import bubble_sort
import insertion_sort
import selection_sort
import merge_sort
import quick_sort
import heap_sort
import visualizer
import shaker_sort


def main():
    run = True
    clock = pygame.time.Clock()

    n = 100
    min_val = 0
    max_val = 100

    lst = visualizer.generate_starting_list(n, min_val, max_val)
    draw_info = visualizer.DrawInformation(1000, 700, lst)
    sorting = False
    ascending = True

    sorting_algorithm = merge_sort.merge_sort
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
            visualizer.draw(draw_info, sorting_algo_name, ascending)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type != pygame.KEYDOWN:
                continue

            if event.key == pygame.K_r:
                lst = visualizer.generate_starting_list(n, min_val, max_val)
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
                sorting_algorithm = insertion_sort.insertion_sort
                sorting_algo_name = "Insertion Sort"
            elif event.key == pygame.K_b and not sorting:
                sorting_algorithm = bubble_sort.bubble_sort
                sorting_algo_name = "Bubble Sort"
            elif event.key == pygame.K_m and not sorting:
                sorting_algorithm = merge_sort.merge_sort
                sorting_algo_name = "Merge Sort"
            elif event.key == pygame.K_q and not sorting:
                sorting_algorithm = quick_sort.quick_sort
                sorting_algo_name = "Quick Sort"
            elif event.key == pygame.K_h and not sorting:
                sorting_algorithm = heap_sort.heap_sort
                sorting_algo_name = "Heap Sort"
            elif event.key == pygame.K_c and not sorting:
                sorting_algorithm = shaker_sort.shaker_sort
                sorting_algo_name = "Shaker Sort"
            elif event.key == pygame.K_s and not sorting:
                sorting_algorithm = selection_sort.selection_sort
                sorting_algo_name = "Selection Sort"

    pygame.quit()


if __name__ == "__main__":
    main()