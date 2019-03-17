#!/usr/bin/env python3

"""This module provides multipale sort function integrate many algorthm:
        - bubble sort
        - insertion sort
        - quick-sort
        - merge sort
        - in-place merge sort
"""


def swap_element(numbers, index_1, index_2):
    """
    swap_element(numbers) -> swap two elements' position.

    This function is used for swaping two elements' position in list numbers.
    If this function runs s, return 0.

    Required arguments:
        numbers     -- list of numbers has elements need to be swaped.
        index_1     -- an integer that is index of first element.
        index_2     -- an integer thar is index of second element.
    """
    try:
        numbers[index_1], numbers[index_2] = numbers[index_2], numbers[index_1]
        return 0
    except IndexError:
        return 1


def run_bubble_sort(numbers):
    """
    run_bubble_sort(numbers)

    The pass through the list is repeated until the list is sorted.
    The algorithm, which is a comparison sort, is named for the way smaller
    or larger elements "bubble" to the top of the list.

    Required arguments:
        numbers     -- list of numbers need to be sorted.
    """

    def do_swap(numbers, loop):
        """
        do_loop(numbers, loop) -> swap element in list still it's sorted.

        This is a sub-function of run_merge_sort(), handle "core-sorting".

        Requried arguments:
            numbers     -- as same as agument of run_bubble_sort()
            loop        -- the times of loop.
        """
        swap = 0    # variable for counting swap's times
        loop = loop - 1
        for i in range(loop):
            if numbers[i] > numbers[i + 1]:
                # swap number, each time swap happen, increas swap by 1
                swap_element(numbers, i, i + 1)
                swap = swap + 1
                print(*numbers)
        return swap

    loop = len(numbers)
    while True:
        # if there is no swap, break the loop
        if do_swap(numbers, loop) == 0:
            break
    return numbers


def run_insertion_sort(numbers):
    """
    run_insertion_sort(numbers) -> implemention of InsertionSort

    Insertion sort is a simple sorting algorithm that works the way we sort
    playing cards in our hands. This function return the sorted numbers.

    Required argument:
        numbers     -- list of numbers need to be sorted.
    """

    def do_sort(numbers):
        """
        do_sort(numbers) -> implemention a step of InsertionSort.

        This function prints the list after each insertion operation
        placing a number at its right place in the sorted list.

        Required argument:
            numbers -- list of numbers
        """
        place = False   # for checking if there is a insertion
        key = numbers[i]
        j = i - 1
        while j >= 0 and key < numbers[j]:
            # Move elements of list_numb[0..i-1], that are greater than key,
            # to one position ahead of thier current position.
            numbers[j + 1] = numbers[j]
            j = j - 1
            # there is a insertion that happened
            place = True
        numbers[j + 1] = key
        if place:
            print(*numbers)

    for i in range(1, len(numbers)):
        do_sort(numbers)
    return numbers


def partition(numbers, left, right):
    """
    partition(numbers, left, right) -> figure out the index of pivot.

    This function return index of pivot, moves the pivot to correct position.

    Required argument:
        numbers     -- list of numbers.
        left        -- index of begin element.
        right       -- index of last element.
    """
    # index of smaller element.
    index = (left - 1)
    # choose last element as pivot.
    pivot_value = numbers[right]
    print("P:", pivot_value)

    for i in range(left, right):
        # If current element is smaller than or equal to pivot.
        if numbers[i] <= pivot_value:
            # increment index of smaller element.
            index = index + 1
            # swap smaller element with current element.
            swap_element(numbers, index, i)
    swap_element(numbers, index + 1, right)
    print(*numbers)
    return index + 1


def run_quick_sort(numbers):
    """
    run_quick_sort(numbers) -> implemention of QuickSort.

    QuickSort is a Divide and Conquer algorithm. It picks an element as
    pivot and partitions the given array around the picked pivot.
    This function use a stack to avoid recursion. Output is the sorted list.

    Required arument:
        numbers     -- list of numbers need to be sorted.
    """

    def pop_push_sort(stack, top, left, right, numbers):
        """
        pop_push_sort(stack, top, left, right, numbers) -> same as recursion.
        """
        # Pop right and left
        right = stack[top]
        top = top - 1
        left = stack[top]
        top = top - 1

        # Set pivot elemet at its correct position in sorted array
        pivot = partition(numbers, left, right)

        # If there are elements on left side of pivot, push left side to stack.
        if pivot - 1 > left:
            top = top + 1
            stack[top] = left
            top = top + 1
            stack[top] = pivot - 1
        # If there are elements on right side of pivot, push them to stack.
        if pivot + 1 < right:
            top = top + 1
            stack[top] = pivot + 1
            top = top + 1
            stack[top] = right
        return top

    # End index is the last index of list.
    right = len(numbers) - 1
    # Begin index is 0.
    left = 0
    # Create an auxiliary stack.
    size = right - left + 1
    stack = [0] * size

    # initialize top of stack
    top = -1

    # push initial values of left and right to stack
    top = top + 1
    stack[top] = left
    top = top + 1
    stack[top] = right

    while top >= 0:
        top = pop_push_sort(stack, top, left, right, numbers)

    return numbers


def run_merge_sort(numbers):
    """
    run_merge_sort(numbers) -> implementaion of MergeSort.

    Merge Sort is a Divide and Conquer algorithm. It divides input array in two
    halves, calls itself for the two halves and then merges the two sorted
    halves. The merge() function is used for merging two halves.
    The merge(arr, left, mid, right) is key process that assumes that
    arr[left..mid] and arr[mid+1..right] are sorted and merges the two sorted
    sub-arrays into one.

    Required argument:
        numbers     -- a list of numbers need to be sorted.
    """

    def copy_data(*args):
        """
        copy_data() -> copy data from numbers to left and right.

        Required arguments:
            arg[0](numbers)     -- a list of numbers need to be sorted
            arg[1](index)       -- index of numbers
            arg[2](left)        -- left array
            arg[3](left_index)  -- index of left
            arg[4](right)       -- right array
            arg[5](right_index) -- index of right
        """
        numbers = args[0]
        index = args[1]
        left = args[2]
        left_index = args[3]
        right = args[4]
        right_index = args[5]
        if left[left_index] < right[right_index]:
            numbers[index] = left[left_index]
            left_index += 1
        else:
            numbers[index] = right[right_index]
            right_index += 1
        index += 1
        return index, left_index, right_index

    if len(numbers) > 1:
        # Mid of array
        mid = int(len(numbers) / 2)
        # First half of array
        left = numbers[:mid]
        # Second half of array
        right = numbers[mid:]
        # Sorting the first half
        run_merge_sort(left)
        # Sorting the second half
        run_merge_sort(right)

        # Create index of array and temp arrays.
        left_index = right_index = index = 0

        # Copy data to temp arrays left[] and right[]
        while left_index < len(left) and right_index < len(right):
            (index,
             left_index,
             right_index) = copy_data(numbers, index,
                                      left, left_index,
                                      right, right_index)

        # Checking if any element was left
        while left_index < len(left):
            numbers[index] = left[left_index]
            left_index += 1
            index += 1
        while right_index < len(right):
            numbers[index] = right[right_index]
            right_index += 1
            index += 1
        print(*numbers)
    return numbers


def run_inplace_merge_sort(numbers, left=0, right=-1):
    """
    run_inplace_merge_sort(numbers, left, right) -> implemention InPlaceMerge.

    Implement Merge Sort i.e. standard implementation keeping the sorting
    algorithm as in-place. In-place means it does not occupy extra memory for
    merge operation as in standard case.
    Time Complexity of above approach is O(n^2 Log n) because merge is O(n^2).
    Time complexity of standard merge sort is less, O(n Log n).

    Required arguments:
        numbers     -- list of numbers need to be sorted.
        left        -- index of left sub-array of numbers.
        right       -- index of right sub-array of numbers.
    """
    if right == -1:
        right = len(numbers) - 1

    def merge(numbers, start, mid, end):
        """
        merge(numbers, start, mid, end) -> Merge two subarrays of numbers.

        Required arguments:
            numbers     -- list of numbers.
            start       -- First index of first subarray numbers[start..mid]
            end         -- Last index of second subarray numbers[mid+1..end]
        """

        def rotate(numbers, start, start_2, mid):
            """
            rotate(numbers, start, start_2, mid) -> rotate 2 sub array.
            """
            value = numbers[start_2]
            index = start_2

            # Shift all the elements between element 1 and element 2 by 1
            while index != start:
                numbers[index] = numbers[index - 1]
                index -= 1
            numbers[start] = value

            # update all the pointers
            start += 1
            mid += 1
            start_2 += 1

            return start, mid, start_2

        # start index of second subarray
        start_2 = mid + 1

        # if the direct merge is already sorted
        if numbers[mid] <= numbers[start_2]:
            return 0

        while start <= mid and start_2 <= end:
            # If element 1 is in right place
            if numbers[start] <= numbers[start_2]:
                start += 1
            else:
                start, mid, start_2 = rotate(numbers, start, start_2, mid)

    if left < right:
        # Same as (left + right) // 2 but  overflow for large left and right.
        mid = left + (right - left) // 2

        # Sort first half
        run_inplace_merge_sort(numbers, left, mid)
        run_inplace_merge_sort(numbers, mid + 1, right)
        # Merge two halves
        merge(numbers, left, mid, right)
        # Print list after every merge.
        print(*numbers)

    return numbers
