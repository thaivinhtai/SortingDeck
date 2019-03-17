#!/usr/bin/env python3

"""This module implement different sorting algorithms and visualise those
algorithms.

When given a series of numbers as input, this module will sort them using the
algorithm specified on the command line. It will output the different steps of
the sorting operation on stdout, or display them in the GUI if the GUI option
is specified.

This module implement the following algorithms:

    - bubble sort
    - insertion sort
    - quick-sort
    - merge sort
"""


from sort_engine import (run_bubble_sort, run_insertion_sort, run_quick_sort,
                         run_merge_sort, run_inplace_merge_sort)
from get_args import get_args


def algorithm(alg, numbers):
    """
    algorithm(alg, numbers)

    This is a manual switcher for select function quickly.

    Required arguments:
        algo    -- a string-type, which is name of sort algorithm.
        numbers -- list of numbers need to be sorted.
    """

    switcher = {
        'bubble': run_bubble_sort,
        'insert': run_insertion_sort,
        'quick': run_quick_sort,
        'merge': run_merge_sort,
        'inplace': run_inplace_merge_sort
    }
    func = switcher.get(alg, None)
    return func(numbers)


def main():
    """
    This is main function.
    """
    numbers, algo, gui = get_args()
    if gui:
        if len(numbers) > 15:
            print("Input too large")
            return 0
    if len(numbers) < 2:
        return 0
    algorithm(algo, numbers)
    return 0


if __name__ == "__main__":
    main()
