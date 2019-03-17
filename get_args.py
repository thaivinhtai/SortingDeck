#!/usr/bin/env python3

"""This module helps get arguments."""


import argparse


def get_args():
    """
    get_args() -> this function uses argparse for get args and do some stuffs
    with them to get data for progressing.

    Return values:

    numbers       -- list of integer arguments.
    args.algo     -- return the algorithm's name.
    args.gui      -- return boolean value, if it is True, the GUI will be
                     displayed.
    """

    parser = argparse.ArgumentParser()
    parser.add_argument('N', nargs='+',
                        help="an integer for the list to sort")
    parser.add_argument('--algo',
                        help="""specify which algorithm
                                to use for sorting among
                                [bubble|insert|quick|merge],
                                default bubble""",
                        default="bubble")
    parser.add_argument('--gui',
                        action='store_true', default=False,
                        help='visualise the algorithm in GUI mode')
    args = parser.parse_args()
    numbers = list()
    for element in args.N:
        numbers.append(int(element))
    return numbers, args.algo, args.gui
