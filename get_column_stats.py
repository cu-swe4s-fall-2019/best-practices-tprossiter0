import sys
import math
import argparse


def calculate_stdev(vec):
    """ Compute standard deviation of a vector/list

    Parameters
    ----------
    vec - takes vector of integers

    Returns
    ----------
    stdev - standard deviation of the vec parameter

    """
    try:  # uses math library, gives standard deviation
        stdev = math.sqrt(sum([(mean-x)**2 for x in V]) / len(V))
        return stdev
    except Exception:
        print("calculation of standard deviation failed")


def calculate_mean(vec):
    """ Compute mean of a vector/list

    Parameters
    ----------
    vec - takes vector of integers

    Returns
    ----------
    mean - arithmetic mean of the vec parameter

    """
    try:  # computes basic arithmetic mean
        mean = sum(V) / len(V)
        return mean
    except Exception:
        "error in dividing sum of column by length of column"


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
                description="Open a file and get mean, stddev of column")

    parser.add_argument('--input_filename',
                        type=str,
                        help='name of input file',
                        required=True)

    parser.add_argument('--column_number',
                        type=int,
                        help='column number to use',
                        required=True)

    args = parser.parse_args()
    print(args)
    file_name = args.input_filename
    col_num = args.column_number

    try:  # code to open file
        file_f = open(file_name, 'r')
    except FileNotFoundError:
        print('file not found')
        sys.exit(1)
    vec_V = []

    try:  # code to assign column to var_V
        for l in file_f:
            A = [int(x) for x in l.split()]
            var_V.append(A[col_num])
    except Exception:
        print("error in trying to parse line to retrieve column")

    try:  # compute mean
        mean = calculate_mean(vec_V)
    except Exception:
        print("error in calling calculate_mean function")

    try:  # compute stdev
        stdev = calculate_stdev(vec_V)
    except Exception:
        print("error in calling calculate_stdev function")

    try:  # return calculated mean
        print('mean:', mean)
    except Exception:
        print("failed to print mean")

    try:  # return calculated stdev
        print('stdev:', stdev)
    except Exception:
        print("failed to print stdev")
