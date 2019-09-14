import sys
import math
import argparse


def calculate_stdev(vec):
    try:
        stdev = math.sqrt(sum([(mean-x)**2 for x in V]) / len(V))
        return stdev
    except Exception:
        print("calculation of standard deviation failed")


def calculate_mean(vec):
    try:
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

    file_name = args[0]
    col_num = args[1]

    try:
        file_f = open(file_name, 'r')
    except FileNotFoundError:
        print('file not found')

    vec_V = []

    try:
        for l in file_f:
            A = [int(x) for x in l.split()]
            var_V.append(A[col_num])
    except Exception:
        print("error in trying to parse line to retrieve column")

    try:
        mean = calculate_mean(vec_V)
    except Exception:
        print("error in calling calculate_mean function")

    try:
        stdev = calculate_stdev(vec_V)
    except Exception:
        print("error in calling calculate_stdev function")

    try:
        print('mean:', mean)
    except Exception:
        print("failed to print mean")

    try:
        print('stdev:', stdev)
    except Exception:
        print("failed to print stdev")
