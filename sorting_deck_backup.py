#!/usr/bin/env python3
import argparse
import random


class Get_args():
    """
    This class uses argparse for get args and do some stuffs with them to get
    data for progressing.
    """

    PARSER = argparse.ArgumentParser()
    PARSER.add_argument('N', nargs='+',
                        help="an integer for the list to sort")
    PARSER.add_argument('--algo',
                        help="""specify which algorithm
                                to use for sorting among
                                [bubble|insert|quick|merge],
                                default bubble""",
                        default="bubble")
    PARSER.add_argument('--gui',
                        action='store_true', default=False,
                        help='visualise the algorithm in GUI mode')
    ARGS = PARSER.parse_args()

    def __init__(self):
        self.N = list()
        for element in self.ARGS.N:
            self.N.append(int(element))
        self.ALGO = self.ARGS.algo
        self.GUI = self.ARGS.gui


def run_bubble_sort(list_numb):
    """
    The pass through the list is repeated until the list is sorted.
    The algorithm, which is a comparison sort, is named for the way smaller
    or larger elements "bubble" to the top of the list.
    """
    loop = len(list_numb)
    while True:
        swap = 0    # variable for counting swap's times
        loop = loop - 1
        for i in range(loop):
            if list_numb[i] > list_numb[i + 1]:
                # swap number, each time swap happen, increas swap by 1
                list_numb[i], list_numb[i + 1] = list_numb[i + 1], list_numb[i]
                swap = swap + 1
                print(*list_numb)
        # if there is no swap, break the loop
        if swap == 0:
            break
    return list_numb


def run_insertion_sort(list_numb):
    """
    Insertion sort is a simple sorting algorithm
    that works the way we sort playing cards in our hands.
    """
    for i in range(1, len(list_numb)):
        place = False   # for checking if there is a insertion
        key = list_numb[i]
        j = i - 1
        while j >= 0 and key < list_numb[j]:
            """
            Move elements of list_numb[0..i-1],
            that are greater than key,
            to one position ahead of thier current position
            """
            list_numb[j + 1] = list_numb[j]
            j = j - 1
            # there is a insertion that happened
            place = True
        list_numb[j + 1] = key
        if place:
            print(*list_numb)
    return list_numb


def run_quick_sort(list_numb, left=0, right=-1, recursion_count=0, sort=True):
    max_recursion = (len(list_numb) // 2) + 1
    swap_count = 0
    if right == -1:
        right = len(list_numb) - 1
    pivot_index = (left + right) // 2
    pivot = list_numb[pivot_index]
    temp_left = left
    temp_right = right
    while True:
        while list_numb[temp_left] < pivot:
            temp_left += 1
        while list_numb[temp_right] > pivot:
            temp_right -= 1
        if temp_left <= temp_right:
            if list_numb[temp_left] != list_numb[temp_right]:
                (list_numb[temp_left],
                 list_numb[temp_right]) = (list_numb[temp_right],
                                           list_numb[temp_left])
                swap_count += 1
                sort = False
            temp_left += 1
            temp_right -= 1
        if temp_left >= temp_right:
            if list_numb[pivot_index] > pivot and list_numb[right] > pivot:
                (list_numb[pivot_index],
                 list_numb[right]) = (list_numb[right],
                                      list_numb[pivot_index])
            break
    if sort:
        if recursion_count < max_recursion:
            print("P: " + str(pivot))
            print(*list_numb)
    else:
        if swap_count > 0:
            print("P: " + str(pivot))
            print(*list_numb)
    if left < temp_right:
        recursion_count += 1
        run_quick_sort(list_numb, left, temp_right, recursion_count, sort)
    if temp_left < right:
        recursion_count += 1
        run_quick_sort(list_numb, temp_left, right, recursion_count, sort)
    return list_numb


def run_merge_sort(list_numb):
    if len(list_numb) > 1:
        mid = int(len(list_numb) / 2)
        left = list_numb[:mid]
        right = list_numb[mid:]
        run_merge_sort(left)
        run_merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                list_numb[k] = left[i]
                i = i + 1
            else:
                list_numb[k] = right[j]
                j = j + 1
            k = k + 1
        while i < len(left):
            list_numb[k] = left[i]
            i = i + 1
            k = k + 1
        while j < len(right):
            list_numb[k] = right[j]
            j = j + 1
            k = k + 1
        print(*list_numb)
    return list_numb


def algorithm(alg, list_numb):
    """
    A manual switcher for select funtion quickly.
    """
    switcher = {
        'bubble': run_bubble_sort,
        'insert': run_insertion_sort,
        'quick': run_quick_sort,
        'merge': run_merge_sort
    }
    func = switcher.get(alg, None)
    return func(list_numb)


def main():
    argv = Get_args()
    if argv.GUI:
        if len(argv.N) > 15:
            print("Input too large")
            return 0
    if len(argv.N) < 2:
        return 0
    algorithm(argv.ALGO, argv.N)
    return 0


if __name__ == "__main__":
    main()
