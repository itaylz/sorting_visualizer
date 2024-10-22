import visualizer

def selection_sort(draw_info, ascending=True):
	lst = draw_info.lst

	for i in range(0, len(lst)-1):
		min = i

		for j in range(i+1, len(lst)):
			if (lst[j] < lst[min] and ascending) or (lst[j] > lst[min] and not ascending):
				min = j

		if min != i:
			lst[min], lst[i] = lst[i], lst[min]
			visualizer.draw_list(draw_info, {min: draw_info.RED, i: draw_info.ORANGE, i + 1: draw_info.YELLOW, i + 2: draw_info.GREEN, i + 3: draw_info.BLUE, i + 4: draw_info.PURPLE},  True)
			yield True

	return lst


